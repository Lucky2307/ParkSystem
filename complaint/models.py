from django.db import models

# Create your models here.

class complaintMessage(models.Model):
    member_id = models.IntegerField()
    #Make it so that even non member can input complaint
    name = models.CharField(max_length=100)
    phone_num = models.CharField(max_length=15)
    #Both should be filled automatically if member
    #(Or make it separate forms for member and non member in front end)
    #If possible make it with session
    vehicle_number = models.CharField(max_length=15)
    complaint_message = models.CharField(max_length=250)
    complaint_date = models.DateField(auto_now=True)