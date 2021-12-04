from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.http import request
from django.utils import timezone

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True,upload_to="static/img/profile")
    website = models.CharField( max_length=50, null=True,blank=True)


    def __str__(self):
        return str(self.user)



class Post(models.Model):
  photo = CloudinaryField('image')
  photo_name = models.CharField(max_length=60)
  posted_at = models.DateTimeField(auto_now_add=True)
  photo_caption = models.TextField()
  user = models.ForeignKey(User,on_delete = models.CASCADE)

  def save_photo(self):
     self.save()

  @classmethod
  def display_photos(cls):
    photos = cls.objects.all().order_by('-posted_at')
    return photos

  @property
  def saved_comments(self):
    return self.comments.all()

  @property
  def saved_likes(self):
    return self.photolikes.count()

  @classmethod
  def search_photos(cls,search_term):
    photos = cls.objects.filter(photo_name__icontains = search_term).all()
    return photos

  def delete_post(self):
    self.delete()

  def __str__(self):
    return "%s photo" % self.photo_name


