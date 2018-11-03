from __future__ import print_function
from django.http import HttpResponse

from inbox.inboxutils import Inbox

inbox = Inbox()


# Create your views here.s
def index(request):
    messages = inbox.get_messages()
    return HttpResponse(messages)
