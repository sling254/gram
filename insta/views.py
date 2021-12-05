from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import Http404,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . forms import postPhotoForm, CreateUserForm,CommentsForm
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from .models import Post,Profile,Like,Comment
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView
from django.views import View

# Create your views here.
class AddLike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)

        is_dislike = False

        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if is_dislike:
            post.dislikes.remove(request.user)

        is_like = False

        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if not is_like:
            post.likes.add(request.user)

        if is_like:
            post.likes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)
class AddDislike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)

        is_like = False

        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if is_like:
            post.likes.remove(request.user)

        is_dislike = False

        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if not is_dislike:
            post.dislikes.add(request.user)

        if is_dislike:
            post.dislikes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)

class ProfileView(View):
    def get(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        user = profile.user
        posts = Post.objects.filter(user=user).order_by('-posted_at')

        context = {
            'user': user,
            'profile': profile,
            'posts': posts
        }

        return render(request, 'profile.html', context)

class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    fields = ['name', 'bio', 'birth_date', 'location', 'profile_photo']
    template_name = 'profile_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('profile', kwargs={'pk': pk})

    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user
#@login_required(login_url='login')
def index(request):
    users = User.objects.all()
    posts = Post.objects.all()
    comments = Comment.objects.all()
    form = CommentsForm()
    title = "i was in June"
    if request.method == 'POST':
        form = CommentsForm(request.POST) 
    if form.is_valid():        
      form = form.save(commit = False)      
      form.author = request.user
      form.save()
      return redirect('index')

    context={
        "title":title,
        "users":users,
        "posts":posts,
        "comments":comments,
        "c_form":form
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


