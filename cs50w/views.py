from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse

# Create your views here.
# def index(request):
 # return HttpResponse("Hello world. you are at blog's index")from django.shortcuts import render
 

# Create your views here.
def index(request):
  return HttpResponse ("Hello world. you are at blog's index")
def detail(response, post_id):
  return HttpResponse ( f"you are at detail post page and Id is {post_id}")
def old_url_redirect(request):
  return redirect(reverse('cs50w:new_page_url'))
def new_url_view(request):
    return HttpResponse("this is new url ")