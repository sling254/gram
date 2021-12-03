from django.shortcuts import render

# Create your views here.


def index(request):
    title = "i was in June"
    context={
        "title":title,
    }

    return render(request,'base.html', context)