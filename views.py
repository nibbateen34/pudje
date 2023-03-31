from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import *

menu = ["About Page", "Add Article", "Feedback", "Log-in"]


def index(request):
    posts = Topigmodelsfyp.objects.all()
    return render(request, 'topigmodelsfyp/index.html', {'menu': menu, 'posts': posts, 'title': 'Main Page'}, )


def about(request):
    return render(request, 'topigmodelsfyp/about.html', {'menu': menu, 'title': 'About Page'})


