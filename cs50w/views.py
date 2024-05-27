from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
def index(request):
  return render(request,"blog/index.html")
def detail(request, post_id):
    return render(request, "blog/detail.html")
 # return HttpResponse ( f"you are at detail post page and Id is {post_id}")
def old_url_redirect(request):
  return redirect("new_url")
def new_url_view(request):
    return HttpResponse("this is new url ")
