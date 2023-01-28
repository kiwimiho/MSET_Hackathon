from django.urls import path
from mood import views

app_name = 'mood'

urlpatterns=[
    path('', views.index, name='index'),
    path('show_mood/',views.show_mood,name='show_mood'),
    path('user_mood',views.user_mood,name='user_mood'),
]