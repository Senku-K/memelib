from django.urls import path
from . import views

urlpatterns = [
    path('', views.meme_list, name='meme_list'),
    path('upload/', views.upload_meme, name='upload_meme'),
    path('download/<int:pk>/', views.download_meme, name='download_meme'),
    path('like/<int:pk>/', views.like_meme, name='like_meme'),
    path('register/', views.register, name='register'),
 
] 
