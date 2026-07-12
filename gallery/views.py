from django.shortcuts import render


def home(request):
    """Show the gallery homepage. The real photo list is added in a later stage."""
    return render(request, 'gallery/home.html')
