from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post,Profile,Comment

# Create your tests here.
class ProfileTestClass(TestCase):

  def setUp(self):
    self.user = User.objects.create_user("me","pass")
    self.profile_test = Profile(profile_photo='https://res.cloudinary.com/dbos9xidr/image/upload/v1626138202/vx39cozmzrnwvofuvuvf.jpg',bio='Student',user=self.user)
    self.profile_test.save()

  def test_instance_true(self):
    self.profile_test.save()
    self.assertTrue(isinstance(self.profile_test,Profile))
        
class TestCommentsClass(TestCase):

  def setUp(self):
    self.test_user = User(username = 'Allan')
    self.test_user.save()
    self.photo = Post(photo = 'new_photo.png',photo_name = 'software photo',photo_caption = 'software engineer',user = self.test_user)
    self.comments = Comment(comment = 'Nice one',photo = self.photo,user = self.test_user)

class TestPostsClass(TestCase):

  def setUp(self):

    self.test_user = User(username = 'Leon')
    self.test_user.save()
    self.photo = Post(photo = 'Leon.jpeg',name = 'Leon',caption = 'Leon',user = self.test_user)
    self.comments = Comment(comment = 'cool',photo = self.photo,user = self.test_user)

  def test_instance(self):
    self.assertTrue(isinstance(self.photo,Post))

    def test_display_photos(self):
    self.photo2= Post(photo = 'me.jpeg',name = 'me',caption = 'me',user = self.test_user)
    self.photo2.save_photo()
    dt = Post.display_photos()
    self.assertEqual(len(dt),2)

  def test_save_photo(self):
    self.photo.save_photo()
    photo = Post.objects.all()
    self.assertTrue(len(photo)>0)

  def test_search(self):
    self.photo.save_photo()
    self.photo2 = Post(photo = 'me.jpeg',name = 'me',caption = 'me',user = self.test_user)
    self.photo2.save_photo()
    search_term = "e"
    search1 = Post.search_photos(search_term)
    search2 = Post.objects.filter(name__icontains = search_term)
    self.assertEqual(len(search2),len(search1))

  def test_delete_photo(self):
    self.photo2 = Post(photo = 'me.jpeg',name = 'me',caption = 'me',user = self.test_user)
    self.photo2.save_photo()
    self.photo.save_photo()
    self.photo.delete_post()
    photos = Post.objects.all()
    self.assertEqual(len(photos),1)
