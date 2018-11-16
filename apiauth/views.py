from django.http import HttpResponseRedirect

from apiauth.authenticate import Authenticator


def index(request):
    authenticator = Authenticator()
    url = authenticator.get_authorization_url(None)
    return HttpResponseRedirect(url)
