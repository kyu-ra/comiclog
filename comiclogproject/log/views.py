from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("hello world, you're at the log index")

def detail(request, id):
    return HttpResponse("You're looking at comic %s." % id)

