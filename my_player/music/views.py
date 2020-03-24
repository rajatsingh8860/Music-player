from django.shortcuts import render
from .models import Info


# Create your views here.
def index(request):
    feed=Info.objects.all()
    return render(request,'music/add.html',{'feed':feed})


def lyr(request,id):
    feedx=Info.objects.all()
    return render(request,'music/lyrics.html',{'feedx':feedx})    
