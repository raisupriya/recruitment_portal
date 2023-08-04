from django.shortcuts import render
from .models import JobListing

def home(request):
    job_listings = JobListing.objects.all()
    return render(request, 'job_portal/home.html', {'job_listings': job_listings})

def add_job_listing(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        location = request.POST['location']
        JobListing.objects.create(title=title, description=description, location=location)
    return render(request, 'job_portal/add_job_listing.html')
