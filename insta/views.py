from django.shortcuts import render

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

    return render(request,'auth/register.html')