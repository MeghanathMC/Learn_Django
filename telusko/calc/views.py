from django.shortcuts import render
from .models import Message
from django.http import HttpResponse
# Create your views here.

def hello_world(request):
    return HttpResponse("<h1>Hello world</h1>")
