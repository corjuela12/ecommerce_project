from django.shortcuts import render

# Create your views here.

from django.http import request

def home(request):
    return render(request, "home/home.html",{}) 