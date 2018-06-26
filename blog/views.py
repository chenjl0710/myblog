from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.

def index(request):
    article = models.article.objects.get(pk=1)
    return render(request,'blog/index.html',{"data":article})
    # return HttpResponse("hello world!")