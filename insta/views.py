from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CreateUserForm

# Create your views here.


def index(request):
    title = "i was in June"
    context={
        "title":title,
    }

    return render(request,'base.html', context)


def login(request):

    return render(request,'auth/login.html')

def register(request):
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