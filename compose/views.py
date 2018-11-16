from django.http import HttpResponse

from compose.compose_utils import ComposeUtils


def compose(request):
    compose_utils = ComposeUtils()
    message = compose_utils.create_message('itisdarshan@gmail.com', 'daas15cs@cmrit.ac.in',
                                           'Darkmail testing', 'Yay it works!')
    compose_utils.send_message('me', message)
    return HttpResponse('Works')
