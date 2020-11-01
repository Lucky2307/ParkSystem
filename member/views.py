from django.shortcuts import render, redirect
from django.urls import reverse
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from .forms import signupForm
from .models import member

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
    return render(request, 'member/signup.html', {'form':form})

def list_members(request):
    members = member.objects.all()
    context = {
        'members': members,
    }
    return render(request, 'member/members.html', context=context)

def edit_member(request, member_id):
    if request.method == 'POST':
        cur_member = member.objects.get(pk=member_id)
        form = signupForm(request.POST, instance=cur_member)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('members'))
    else:
        cur_member = member.objects.get(pk=member_id)
        fields = model_to_dict(cur_member)
        form = signupForm(initial=fields, instance=cur_member)
    context = {
        'form': form,
        'type': 'edit',
    }
    return render(request, 'member/signup.html', context=context)

def delete_member(request, member_id):
    cur_member = member.objects.get(pk=member_id)
    if request.method == 'POST':
        cur_member.delete()
        return HttpResponseRedirect(reverse('members'))
    context = {
        'member': cur_member
    }
    return render(request, 'member/members.html', context=context)