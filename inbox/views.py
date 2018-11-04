from __future__ import print_function

from django.shortcuts import render

from inbox.inboxutils import Inbox

inbox = Inbox()


# Create your views here.s
def index(request):
    messages = inbox.get_messages()
    return render(request, 'inbox/inbox.html', {'messages': messages})
