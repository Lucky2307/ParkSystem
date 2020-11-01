from django.shortcuts import render
from django.http import HttpResponse
from complaint.models import complaintMessage
from member.models import member
from datetime import date, timedelta

# Create your views here.

def index(request):
    memberCount = member.objects.all().count()
    complaintTotalCount = complaintMessage.objects.all().count()
    complaintCount = [0,0,0,0,0,0,0]
    baseDate = date.today()
    for day in range(7):
        complaintCount[6-day] = complaintMessage.objects.filter(complaint_date=baseDate - timedelta(days=day)).count()
    return render(request, 'dashboard.html', {'memberCount':memberCount, 'complaintTotalCount':complaintTotalCount , 'complaintCount':complaintCount})

def success(request):
    return render(request, 'success.html', {})