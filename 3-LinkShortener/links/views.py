from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Link
from .forms import LinkForm

def index(request):
    context = { "links": Link.objects.all() }
    return render(request, 'links/index.html', context)


def root_link(request, link_slug):
    link = get_object_or_404(Link, slug=link_slug)
    link.click()
    return redirect(link.url)


def add_link(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            form.save()
            redirect(reverse('home'))
    else:
        form = LinkForm()        
    
    return render(request, 'links/create.html', { 'form': form })
