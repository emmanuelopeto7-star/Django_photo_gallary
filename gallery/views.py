from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import ProfileForm, RegisterForm
from .models import Photo, Profile


def home(request):
    """Show every photo in the gallery, newest first."""
    photos = Photo.objects.all().order_by('-created_at')
    return render(request, 'gallery/home.html', {'photos': photos})


def register(request):
    """Let a new user create an account, then log them straight in."""
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('gallery_home')
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form})


@login_required
def profile(request):
    """Show and let the logged-in user edit their profile."""
    user_profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=user_profile)

    return render(request, 'gallery/profile.html', {'form': form})
