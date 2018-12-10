from __future__ import print_function

from django.shortcuts import render

from inbox.inbox_utils import InboxUtils


def inbox(request):
    inbox_utils = InboxUtils(request.session.get('access_token'),
                             request.META['HTTP_USER_AGENT'])
    messages = [parse_to_context(m) for m in inbox_utils.get_messages()]
    context = {'messages': messages}
    return render(request, 'inbox/inbox.html', context)


def details(request, message_id):
    inbox_utils = InboxUtils(request.session.get('access_token'),
                             request.META['HTTP_USER_AGENT'])
    message = parse_to_context(inbox_utils.get_detailed_message(message_id))
    context = {'message': message}
    return render(request, 'inbox/details.html', context)


def parse_to_context(m: dict):
    message = {}
    for key, value in m.items():
        if key == 'payload':
            for header in m['payload']['headers']:
                message[header['name']] = header['value']
        else:
            message[key] = value
    return message
