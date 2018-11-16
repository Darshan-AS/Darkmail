from django.urls import path

from apiauth import views

app_name = 'apiauth'

urlpatterns = [
    path('', views.index, name='compose'),
]
