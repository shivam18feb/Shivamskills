from django.urls import path
from .import views
urlpatterns=[
    path('serv/',views.serv, name='serv')
]