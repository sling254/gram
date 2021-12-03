from django.shortcuts import render

# Create your views here.


def index():
    title = "i was in June"
    context={
        "title":title,
    }

    return render('base.html', context)