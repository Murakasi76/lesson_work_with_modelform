from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from ex_1.forms import FormAuthor

# Create your views here.

def index(request: HttpRequest):
    if request.method == "GET":
        form = FormAuthor()
        context = {
            "form": form,
        }
        
        return render(request, "ex_1/index.html", context)
    if request.method == "POST":
        form = FormAuthor(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("The author was created")
        