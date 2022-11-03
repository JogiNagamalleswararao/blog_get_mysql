from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
def app(request):
    post=Blog.objects.all()
    return render(request,"base.html",{'post':post})
# Create your views here.
