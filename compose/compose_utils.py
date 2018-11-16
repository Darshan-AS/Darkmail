import base64
from email.mime.text import MIMEText

from googleapiclient import errors

from apiauth.authenticate import Authenticator


class ComposeUtils:

    def __init__(self, auth_code=None):
        authenticator = Authenticator()
        self.__service = authenticator.get_service(auth_code)

    def create_message(self, sender, to, subject, message_text):
        message = MIMEText(message_text)
        message['to'] = to
        message['from'] = sender
        message['subject'] = subject
        return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')}

    def send_message(self, user_id, message):
        try:
            message = (self.__service.users().messages().send(userId=user_id, body=message)
                       .execute())
            print('Message Id: %s' % message['id'])
            return message
        except errors.HttpError as error:
            print('An error occurred: %s' % error)
