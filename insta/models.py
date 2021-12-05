from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.utils import timezone
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField

# Create your models here.
 


class Profile(models.Model):
  profile_photo = CloudinaryField('image', blank=True)
  bio = models.TextField()
  name = models.CharField(max_length=30, blank=True, null=True)
  bio = models.TextField(max_length=500, blank=True, null=True)
  birth_date=models.DateField(null=True, blank=True)
  location = models.CharField(max_length=100, blank=True, null=True)
  user = models.OneToOneField(User, primary_key=True, verbose_name='user', related_name='profile', on_delete=models.CASCADE)
  followers = models.ManyToManyField(User, blank=True, related_name='followers')
  


  @receiver(post_save , sender = User)
  def create_profile(instance,sender,created,**kwargs):
    if created:
      Profile.objects.create(user = instance)

  @receiver(post_save,sender = User)
  def save_profile(sender,instance,**kwargs):
    instance.profile.save()



  def __str__(self):
    return "%s profile" % self.user

class Post(models.Model):
  photo = CloudinaryField('image')
  photo_name = models.CharField(max_length=100)
  posted_at = models.DateTimeField(auto_now_add=True)
  photo_caption = models.TextField()
  user = models.ForeignKey(User,on_delete = models.CASCADE)
  likes = models.ManyToManyField(User, blank=True, related_name='likes')
  dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes')


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




class Like(models.Model):
  image =models.ForeignKey(Post, on_delete = models.CASCADE,related_name='photolikes')
  liker=models.ForeignKey(User,on_delete = models.CASCADE,related_name='userlikes')

  def __str__(self):
    return "%s like" % self.photo



class Comment(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE,blank=True, null=True)
    



    def __str__(self):
      return self.comment