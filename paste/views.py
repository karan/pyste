from django.shortcuts import render, get_object_or_404
from paste.models import Paste

def index(request):
    # get the pastes that are published
    pastes = Paste.objects.all()
    # now return the rendered template
    return render(request, 'paste/index.html', {'pastes': pastes})

def paste(request, slug):
    # get the Post object
    paste = get_object_or_404(Paste, slug=slug)
    # now return the rendered template
    return render(request, 'paste/paste.html', {'paste': paste})