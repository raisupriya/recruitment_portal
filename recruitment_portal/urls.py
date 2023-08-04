from django.urls import path
from job_portal import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_job_listing/', views.add_job_listing, name='add_job_listing'),
]
