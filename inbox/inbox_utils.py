import base64
import email

from googleapiclient import errors

from apiauth.authenticate import Authenticator


class InboxUtils:

    def __init__(self, access_token, user_agent):
        authenticator = Authenticator()
        self.__service = authenticator.get_service(access_token, user_agent)

    def get_messages(self):
        response = self.__service.users().messages().list(
            userId='me', maxResults=10, labelIds=['INBOX']).execute()
        messages_list = []
        if 'messages' in response:
            messages_list.extend(response['messages'])

        '''
        while 'nextPageToken' in response:
            page_token = response['nextPageToken']
            response = self.service.users().messages().list(
                userId='me', q='', pageToken=page_token).execute()
            messages.extend(response['messages'])
        '''

        messages = []
        for message in messages_list:
            try:
                m = self.__service.users().messages().get(
                    userId='me', id=message['id'], format='metadata',
                    metadataHeaders=['To', 'From', 'Subject', 'Date']).execute()

                messages.append(m)

            except errors.HttpError as error:
                print('An error occurred: %s', error)

        return messages

    def get_detailed_message(self, message_id):
        global mime_msg, m, message
        try:
            m = self.__service.users().messages().get(
                userId='me', id=message_id, format='raw').execute()

            message = self.__service.users().messages().get(
                userId='me', id=message_id, format='metadata').execute()

            msg_str = base64.urlsafe_b64decode(m['raw'].encode('ASCII')).decode("utf-8")
            mime_msg = email.message_from_string(msg_str)

        except errors.HttpError as error:
            print('An error occurred: %s', error)

        decoded_message = ''
        for part in mime_msg.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            name = part.get_param("name")
            content_type = part.get_content_type()
            if name is None and content_type == 'text/html':
                decoded_message += part.get_payload(decode=1).decode("utf-8")

        message['body'] = decoded_message

        return message
