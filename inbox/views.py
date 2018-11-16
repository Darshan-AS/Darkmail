from __future__ import print_function

from django.shortcuts import render

from inbox.inbox_utils import InboxUtils


# Create your views here.s
def inbox(request):
    auth_code = request.GET.get('code')
    request.session['authorization_code'] = auth_code
    inbox_utils = InboxUtils(auth_code)
    messages = inbox_utils.get_messages()
    context = {'messages': messages}
    return render(request, 'inbox/inbox.html', context)


def details(request, message_id):
    inbox_utils = InboxUtils()
    detailed_message = inbox_utils.get_detailed_message(message_id)
    context = {'message_body': detailed_message}
    return render(request, 'inbox/details.html', context)
