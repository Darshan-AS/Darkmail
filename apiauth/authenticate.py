from __future__ import print_function

import logging
from importlib import import_module

import httplib2
from django.conf import settings
from googleapiclient import errors
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client.client import FlowExchangeError, AccessTokenCredentials
from oauth2client.client import flow_from_clientsecrets

from Darkmail.settings import BASE_DIR

SessionStore = import_module(settings.SESSION_ENGINE).SessionStore


class Authenticator:
    CLIENTSECRETS_LOCATION = BASE_DIR + '/client_secret.json'
    REDIRECT_URI = 'http://127.0.0.1:8000/login'
    SCOPES = [
        'https://www.googleapis.com/auth/gmail.readonly',
        'https://www.googleapis.com/auth/userinfo.email',
        'https://www.googleapis.com/auth/userinfo.profile',
        'https://www.googleapis.com/auth/gmail.send',
    ]

    def __init__(self):
        pass

    def get_authorization_url(self, email_address=None, state=None):
        flow = flow_from_clientsecrets(self.CLIENTSECRETS_LOCATION, ' '.join(self.SCOPES),
                                       redirect_uri=self.REDIRECT_URI)
        flow.params['access_type'] = 'offline'
        flow.params['approval_prompt'] = 'force'
        flow.params['user_id'] = email_address
        flow.params['state'] = state
        authorization_url = flow.step1_get_authorize_url(self.REDIRECT_URI, state)
        return authorization_url

    def get_service(self, access_token, user_agent):
        credentials = AccessTokenCredentials(access_token, user_agent)
        service = build('gmail', 'v1', http=credentials.authorize(Http()))
        return service

    def exchange_code(self, authorization_code):
        flow = flow_from_clientsecrets(self.CLIENTSECRETS_LOCATION, ' '.join(self.SCOPES),
                                       redirect_uri=self.REDIRECT_URI)
        try:
            credentials = flow.step2_exchange(authorization_code)
            return credentials
        except FlowExchangeError as error:
            logging.error('An error occurred: %s', error)
            raise CodeExchangeException(None)

    def get_credentials(self, authorization_code, state=None):
        email_address = ''
        try:
            credentials = self.exchange_code(authorization_code)
            user_info = self.get_user_info(credentials)
            email_address = user_info.get('email')
            user_id = user_info.get('id')
            if credentials.refresh_token is not None:
                return credentials, email_address

        except CodeExchangeException as error:
            logging.error('An error occurred during code exchange.')
            error.authorization_url = self.get_authorization_url(email_address, state)
            raise error
        except NoUserIdException:
            logging.error('No user ID could be retrieved.')

        authorization_url = self.get_authorization_url(email_address, state)
        raise NoRefreshTokenException(authorization_url)

    def get_user_info(self, credentials):
        user_info_service = build(
            serviceName='oauth2', version='v2',
            http=credentials.authorize(httplib2.Http()))
        user_info = None
        try:
            user_info = user_info_service.userinfo().get().execute()
        except errors.HttpError as e:
            logging.error('An error occurred: %s', e)
        if user_info and user_info.get('id'):
            return user_info
        else:
            raise NoUserIdException()


class GetCredentialsException(Exception):
    def __init__(self, authorization_url):
        """Construct a GetCredentialsException."""
        self.authorization_url = authorization_url


class CodeExchangeException(GetCredentialsException):
    """Error raised when a code exchange has failed."""


class NoRefreshTokenException(GetCredentialsException):
    """Error raised when no refresh token has been found."""


class NoUserIdException(Exception):
    """Error raised when no user ID could be retrieved."""
