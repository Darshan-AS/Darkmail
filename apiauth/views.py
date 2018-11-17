from django.shortcuts import render, redirect
from django.urls import reverse

from apiauth.authenticate import Authenticator

authenticator = Authenticator()

def index(request):
    login_url = reverse('apiauth:login')
    return render(request, 'index.html', context={'url': login_url})


def login(request):
    if 'code' in request.GET:
        c, u = authenticator.get_credentials(
            request.GET.get('code'), request.GET.get('state'))
        request.session['username'] = u
        request.session['access_token'] = c.access_token

    if 'username' in request.session and 'access_token' in request.session:
        return redirect('inbox:inbox')

    return redirect(authenticator.get_authorization_url())


def logout(request):
    request.session.flush()
    return redirect('apiauth:index')
