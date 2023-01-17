from django.shortcuts import render

# HttpResponse를 이용하기 위한 import
from django.http import HttpResponse


# Create your views here.

def index(request) :
    return HttpResponse("Django TEST")