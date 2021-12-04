from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True,upload_to="static/img/profile")
    website = models.CharField( max_length=50, null=True,blank=True)


    def __str__(self):
        return str(self.user)