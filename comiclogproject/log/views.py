from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Comic
from .ref import ComicRef as ref

def index(request):
    latest_comic_list = Comic.objects.order_by("-pub_date")[:5]
    context = {"latest_comic_list": latest_comic_list}
    return render(request, "log/index.html", context)

def detail(request, id):
    comic = get_object_or_404(Comic, pk=id)
    return(render(request, "log/detail.html", {"comic": comic}))

