from django.urls import path

from inbox import views

app_name = 'inbox'

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('<str:messageid>', views.details, name='details')
]
