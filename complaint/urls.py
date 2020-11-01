from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('message/', views.confirmMessage, name="message"),
    path('complaints/', views.list_complaints, name='complaints'),
]
