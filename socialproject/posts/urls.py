from django.db.models import CharField

from .views import post_create, feed, like_post
from django.urls import path

urlpatterns = [
    path('create/',post_create,name='create'),
    path('feed/',feed,name='feed'),
    path('like/',like_post,name='like')
]