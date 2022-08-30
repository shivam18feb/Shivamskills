from django.urls import path
from .import views
urlpatterns =[
    path('Edu/',views.Edu, name='Edu')
]