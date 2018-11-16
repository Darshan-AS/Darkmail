from django.urls import path

from compose import views

app_name = 'compose'

urlpatterns = [
    path('', views.compose, name='compose'),
]
