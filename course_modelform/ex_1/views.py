from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def index(request: HttpRequest):
    if request.method == "GET":
        context = {
            
        }
        
        return HttpResponse("Hello", context)
        