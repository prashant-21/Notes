from django.shortcuts import render


def index(request):
    """The home page for the Web App."""
    return render(request, 'notes/index.html')
