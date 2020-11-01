from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('members/', views.list_members, name='members'),
    path('edit/<int:member_id>', views.edit_member, name='edit_member'),
    path('delete/<int:member_id>', views.delete_member, name='delete_member'),
]
