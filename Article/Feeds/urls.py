from django.urls import path,include
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    
    path('lo/',Login.as_view(),name='lo'),
    path('create/',login_required(post.as_view()),name='create'),
    path('',postList.as_view(),name='list'),
    path('comment/',comment.as_view(),name='comment'),
    path('follwer/',login_required(Followers.as_view()),name='follower'),
    path('save/',login_required(Draft.as_view()),name='save'),
    path('edit/<int:pk>',login_required(Edit.as_view()),name='edit')
    
]
