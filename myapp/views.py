from django.shortcuts import render, redirect
from .models import Recruiter
from .forms import RecruiterForm

def add_recruiter(request):
    if request.method == 'POST':
        form = RecruiterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_recruiters')
    else:
        form = RecruiterForm()
    
    return render(request, 'add_recruiter.html', {'form': form})

def list_recruiters(request):
    recruiters = Recruiter.objects.all()
    return render(request, 'list_recruiters.html', {'recruiters': recruiters})
