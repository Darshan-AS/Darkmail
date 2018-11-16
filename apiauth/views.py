from django.shortcuts import render, redirect
from django.urls import reverse

from apiauth.authenticate import Authenticator

authenticator = Authenticator()

def index(request):
    if Authenticator.SESSION.get('credentials') is None:
        url = authenticator.get_authorization_url()
    else:
        url = reverse('inbox:inbox')

    return render(request, 'index.html', context={'url': url})


def login(request):
    auth_code = request.GET.get('code')
    authenticator.get_credentials(auth_code)

    return redirect('inbox:inbox')


def logout(request):
    if Authenticator.SESSION.get('credentials') is not None:
        Authenticator.SESSION['credentials'] = None
    return redirect('apiauth:index')
