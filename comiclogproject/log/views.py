from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Comic

def index(request):
    latest_comic_list = Comic.objects.order_by("-pub_date")[:5]
    context = {"latest_comic_list": latest_comic_list}
    return render(request, "log/index.html", context)

def detail(request, id):
    return HttpResponse("You're looking at comic %s." % id)

