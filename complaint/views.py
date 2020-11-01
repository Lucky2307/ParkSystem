from django.shortcuts import render, redirect
from django.urls import reverse
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from .forms import complaintMessageForm
from .models import complaintMessage

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

def list_complaints(request):
    complaints = complaintMessage.objects.all()
    context = {
        'complaints': complaints,
    }
    return render(request, 'complaint/complaints.html', context=context)

def edit_complaint(request, complaint_id):
    if request.method == 'POST':
        cur_complaint = complaintMessage.objects.get(pk=complaint_id)
        form = complaintMessageForm(request.POST, instance=cur_complaint)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('complaints'))
    else:
        cur_complaint = complaintMessage.objects.get(pk=complaint_id)
        fields = model_to_dict(cur_complaint)
        form = complaintMessageForm(initial=fields, instance=cur_complaint)
    context = {
        'form': form,
        'type': 'edit',
        'id': complaint_id,
    }
    return render(request, 'complaint/message.html', context=context)

def delete_complaint(request, complaint_id):
    cur_complaint = complaintMessage.objects.get(pk=complaint_id)
    cur_complaint.delete()
    return HttpResponseRedirect(reverse('complaints'))
