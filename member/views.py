from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import signupForm

# Create your views here.

def index(request):
    return HttpResponse("HomeView")

def signup(request):
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = signupForm()
    
    return render(request, 'complaint/message.html', {'form':form})