from django.urls import path
from mood import views

app_name = 'mood'

urlpatterns=[
    path('', views.index, name='index'),
]