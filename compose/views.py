from django.http import HttpResponse
from django.shortcuts import render, redirect

from compose.compose_utils import ComposeUtils


def compose(request):
    return render(request, 'compose/compose.html')


def send(request):
    if request.method != 'POST':
        return redirect('compose:compose')

    to = request.POST['to']
    subject = request.POST['subject']
    body = request.POST['body']

    compose_utils = ComposeUtils(request.session.get('access_token'),
                                 request.META['HTTP_USER_AGENT'])
    message = compose_utils.create_message('itisdarshan@gmail.com', to, subject, body)
    compose_utils.send_message('me', message)

    return HttpResponse(to + '\n' + subject + '\n' + body)
