from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='gallery_home'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('photo/<int:pk>/', views.photo_detail, name='photo_detail'),
]
