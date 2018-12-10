from __future__ import print_function

from pprint import pprint

from django.shortcuts import render

from inbox.inbox_utils import InboxUtils


def inbox(request):
    inbox_utils = InboxUtils(request.session.get('access_token'),
                             request.META['HTTP_USER_AGENT'])
    messages_data = inbox_utils.get_messages()
    messages = []
    for m in messages_data:
        message = {
            'id': m['id'],
            'threadId': m['threadId'],
            'labelIds': m['labelIds'],
            'snippet': m['snippet']
        }
        for header in m['payload']['headers']:
            message[header['name']] = header['value']
        messages.append(message)

    context = {'messages': messages}
    pprint(context)
    """
    {
        'id': '16796c04c49506db', 
        'threadId': '16796c04c49506db', 
        'labelIds': ['IMPORTANT', 'CATEGORY_UPDATES', 'INBOX'], 
        'snippet': 'Hello! We hope that you are actively participating in the Microsoft AI Challenge. We did a webinar with a small group of people and are releasing the video of same here: https://1drv.ms/v/s!', 
        'historyId': '658068', 
        'internalDate': '1544422404000', 
        'payload': {
            'mimeType': 'multipart/alternative', 
            'headers': [
                {
                    'name': 'From', 
                    'value': 'Kedhar Nath Narahari <kedharn@microsoft.com>'
                }, 
                {
                    'name': 'Subject', 
                    'value': 'Help video for Microsoft AI Challenge'
                }, 
                {
                    'name': 'Date', 
                    'value': 'Mon, 10 Dec 2018 06:13:24 +0000'
                }
            ]
        },
         'sizeEstimate': 53117
     }
    """
    return render(request, 'inbox/inbox.html', context)


def details(request, message_id):
    inbox_utils = InboxUtils(request.session.get('access_token'),
                             request.META['HTTP_USER_AGENT'])
    detailed_message = inbox_utils.get_detailed_message(message_id)
    context = {'message_body': detailed_message}
    return render(request, 'inbox/details.html', context)
