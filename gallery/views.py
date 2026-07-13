from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PhotoForm, ProfileForm, RegisterForm
from .models import Photo, Profile, Tag


def home(request):
    """Show every photo in the gallery, newest first.

    If a ?tag=name query parameter is given, only show photos that
    have that tag.
    """
    photos = Photo.objects.all().order_by('-created_at')

    selected_tag = request.GET.get('tag')
    if selected_tag:
        photos = photos.filter(tags__name=selected_tag)

    context = {
        'photos': photos,
        'tags': Tag.objects.all(),
        'selected_tag': selected_tag,
    }
    return render(request, 'gallery/home.html', context)


def photo_detail(request, pk):
    """Show one photo's title, description, and tags."""
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'gallery/photo_detail.html', {'photo': photo})


@login_required
def upload_photo(request):
    """Let a logged-in user add a new photo to the gallery."""
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.uploaded_by = request.user
            photo.save()
            form.save_m2m()
            return redirect('photo_detail', pk=photo.pk)
    else:
        form = PhotoForm()

    return render(request, 'gallery/upload_photo.html', {'form': form})


@login_required
def like_photo(request, pk):
    """Like a photo. Liking a photo you had disliked removes the dislike.
    Liking a photo you already liked removes the like (un-like)."""
    photo = get_object_or_404(Photo, pk=pk)
    photo.disliked_by.remove(request.user)

    if request.user in photo.liked_by.all():
        photo.liked_by.remove(request.user)
    else:
        photo.liked_by.add(request.user)

    return redirect('photo_detail', pk=pk)


@login_required
def dislike_photo(request, pk):
    """Dislike a photo. Works the same way as like_photo, but the other
    way around."""
    photo = get_object_or_404(Photo, pk=pk)
    photo.liked_by.remove(request.user)

    if request.user in photo.disliked_by.all():
        photo.disliked_by.remove(request.user)
    else:
        photo.disliked_by.add(request.user)

    return redirect('photo_detail', pk=pk)


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
