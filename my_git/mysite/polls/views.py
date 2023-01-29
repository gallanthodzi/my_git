# from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("hello, my good people, i just wrote my first poll app view")
# Create your views here.
