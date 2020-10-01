from django.db import models
from real_User.models import RealUser

# Create your models here.

class userInformation(models.Model):
    imageName= models.CharField(max_length= 100, blank=False)
    Image = models.FileField( upload_to= 'images/dataImage', blank=True)
    Date = models.CharField(max_length=100, blank=False)
    Time = models.CharField(max_length= 100, blank= True)

    realuser = models.ForeignKey(RealUser,null=True, on_delete=models.CASCADE)

