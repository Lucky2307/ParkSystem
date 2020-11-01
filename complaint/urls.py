from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('message/', views.confirmMessage, name="message"),
    path('complaints/', views.list_complaints, name='complaints'),
    path('edit/<int:complaint_id>', views.edit_complaint, name='edit_complaint'),
    path('delete/<int:complaint_id>', views.delete_complaint, name='delete_complaint'),
]
