from django.shortcuts import render
from .models import Job
from django.shortcuts import get_object_or_404

def homePage(request):
    jobs = Job.objects
    return render(request,'jobs/homePage.html', {'jobs':jobs})


def detail(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/detail.html', {'job':job_detail})
