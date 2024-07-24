from django.shortcuts import render
from . import models

# Create your views here.
def index(request):
    posts = models.Post.objects.all()
    return render(request, 'index.html', {'posts' : posts})