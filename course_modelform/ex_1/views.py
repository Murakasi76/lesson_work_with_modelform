from django.shortcuts import render, redirect
from django.http import HttpRequest
from ex_1.forms import FormAuthor, FormBook
from ex_1.models import Author, Book

# Create your views here.

# def index(request: HttpRequest):
#     if request.method == "GET":
#         form = FormAuthor()
#         context = {
#             "form": form,
#         }
        
#         return render(request, "ex_1/index.html", context)
#     if request.method == "POST":
#         form = FormAuthor(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("The author was created")



def index(request: HttpRequest):
    if request.method == "POST":
        author_form = FormAuthor(request.Post, prefix="author")
        book_form = FormBook(request.POST, prefix="book")
        if author_form.is_valid() and book_form.is_valid():
            author: Author = author_form.save()
            book: Book = book_form.save()
            book.author = author
            book.save()
            return redirect("success_page")
    else:
        author_form = FormAuthor(prefix="author")
        book_form = FormBook(prefix="book")
    context = {
        "author_form": author_form,
        "book_form": book_form,
    }
    return render(request, "ex_1/index.html", context)
        