from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [
    # API to Post Comment
    path('postComment', views.postComment, name="postComment"),
    # path('like/<int:pk>', views.LikeView, name="like_post"),
    path('', views.blogHome, name='blogHome'),
    path('<str:slug>', views.blogPost, name='blogPost'),
]