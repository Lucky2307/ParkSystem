from django.db import models

# Create your models here.
class member(models.Model):
    member_id = models.AutoField(primary_key=True, serialize=True)
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    dob = models.DateField()
    phone_num = models.CharField(max_length=15)
    address = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.member_id} - {self.name}'