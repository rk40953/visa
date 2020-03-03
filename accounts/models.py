from django.db import models


# Create your models here.

class person_inquir(models.Model):
    first_name=models.CharField(max_length=85)
    last_name=models.CharField(max_length=75)
    email=models.EmailField()
    phone_number=models.CharField(max_length=15)
    message=models.TextField(max_length=500)
    usa=models.BooleanField(default=False)
    australia=models.BooleanField(default=False)
    canada=models.BooleanField(default=False)
    united_kingdom=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)



    

