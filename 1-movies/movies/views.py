from django.shortcuts import render

def index(request):
    context = {
        'movies': [
            "Red, White and Royal Blue",
            "Howl's Moving Castle",
            "The Fault in our Stars",
            "The Suicide Squad",
            "Million Dollar Baby",
            "Five Feet Apart"
        ]
    }
    return render(request, 'movies/index.html', context)

def about(request):
    return render(request, 'movies/about.html', {})