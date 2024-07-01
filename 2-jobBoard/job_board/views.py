from django.shortcuts import render
from .models import JobPosting

def index(request):
    context = {
        'job_postings':  JobPosting.objects.filter(is_active=True)
    }
    return render(request, "job_board/index.html", context)
    
def job_detail(request, pk):
    context = {
        'posting':  JobPosting.objects.get(pk=pk)
    }
    return render(request, "job_board/detail.html", context)
