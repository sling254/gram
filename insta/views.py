from django.shortcuts import render,redirect, get_object_or_404
from django.http import Http404,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . forms import postPhotoForm, CreateUserForm
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from .models import Post,Profile
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.




@login_required(login_url='login')
def index(request):
    users = User.objects.all()
    title = "i was in June"
    context={
        "title":title,
        "users":users,
    }

    return render(request,'index.html', context)

@login_required
def post(request):
  if request.method == 'POST':
    post_form = postPhotoForm(request.POST,request.FILES) 
    if post_form.is_valid():        
      the_post = post_form.save(commit = False)
      
      the_post.user = request.user
      the_post.save()
      return redirect('index')

  else:
    post_form = postPhotoForm()
  return render(request,'post.html',{"post_form":post_form})





def loginView(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            username=request.POST.get('username')
            password=request.POST.get('password')

            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('index')
            else:
                messages.info(request,'Username or password is in correct')

        return render(request,'auth/login.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Account created for' + user ) 
                return redirect('login')
        context={
            "form":form
        }

    return render(request,'auth/register.html',context)


def logoutuser(request):
    logout(request)
    return redirect ('login')


def profileview(request):
    context={}

    return render(request, "profile.html",context)