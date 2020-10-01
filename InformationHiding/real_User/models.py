from django.db import models

# Create your models here.
class RealUser(models.Model):
    userName = models.CharField(max_length=100, blank= False, unique= True)
    FirstName= models.CharField(max_length=100, blank= True)
    LastName = models.CharField(max_length=100, blank= True)
    Phone_No = models.IntegerField(blank=True, null= True)
    EmailID = models.EmailField(max_length=100, unique= True)
    Occupation = models.CharField(max_length=100, blank= True)
    City = models.CharField(max_length= 100, blank= True)
    Country = models.CharField(max_length=100,blank=True)


    def __str__(self):
        return self.userName

