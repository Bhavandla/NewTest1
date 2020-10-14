from django.urls import path
from blog import views

urlpatterns = [
    path('posts', views.post_list, name='post_list'),
    path('index', views.index, name='post_list'),
]