from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, fields
from django import forms
from .models import Post,Comment



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1','password2']

class postPhotoForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['photo','photo_name','photo_caption']



class CommentsForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['comment']
  
    
