from django.shortcuts import render, redirect

from compose.compose_utils import ComposeUtils


def compose(request):
    return render(request, 'compose/compose.html')


def send(request):
    if request.method != 'POST':
        return redirect('compose:compose')

    to = request.POST['to']
    subject = request.POST['subject']
    body = request.POST['message']

    compose_utils = ComposeUtils(request.session.get('access_token'),
                                 request.META['HTTP_USER_AGENT'])
    message = compose_utils.create_message('me', to, subject, body)
    compose_utils.send_message('me', message)

    return redirect('inbox:inbox')
