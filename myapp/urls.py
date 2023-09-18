from django.urls import path
from . import views

urlpatterns = [
    path('add_recruiter/', views.add_recruiter, name='add_recruiter'),
    path('list_recruiters/', views.list_recruiters, name='list_recruiters'),
]
