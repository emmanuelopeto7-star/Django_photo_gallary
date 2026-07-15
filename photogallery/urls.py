"""photogallery URL Configuration"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from gallery.forms import LoginForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='registration/login.html', authentication_form=LoginForm),
        name='login',
    ),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path(
        'password-change/',
        auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),
        name='password_change',
    ),
    path(
        'password-change/done/',
        auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
        name='password_change_done',
    ),
    path('', include('gallery.urls')),
]
