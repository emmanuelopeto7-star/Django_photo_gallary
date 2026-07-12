from django.contrib.auth import login
from django.shortcuts import redirect, render

from .forms import RegisterForm


def home(request):
    """Show the gallery homepage. The real photo list is added in a later stage."""
    return render(request, 'gallery/home.html')


def register(request):
    """Let a new user create an account, then log them straight in."""
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('gallery_home')
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form})
