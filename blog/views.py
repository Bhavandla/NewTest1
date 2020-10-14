from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def post_list(request):
    return render(request, 'base/post_list.html', {})


def index(request):
    return HttpResponse("<h1>This is Index/Baqse Page<h1>")
