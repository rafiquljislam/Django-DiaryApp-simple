from django.shortcuts import render,redirect
from . models import nodebook

# Create your views here.

def index(request):
    texts = nodebook.objects.all()
    return render(request,'notebook/index.html',{'texts':texts})

def add(request):
    if request.method == "POST":
        text = request.POST['text']
        a = nodebook(text=text)
        a.save()
        return redirect('home')
    return render(request,'notebook/add.html')