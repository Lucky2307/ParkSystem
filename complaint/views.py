from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import complaintMessageForm

# Create your views here.

def confirmMessage(request):
    if request.method == 'POST':
        form = complaintMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = complaintMessageForm()
    
    return render(request, 'complaint/message.html', {'form':form})
