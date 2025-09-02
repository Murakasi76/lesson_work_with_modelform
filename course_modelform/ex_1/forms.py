from django import forms
from ex_1.models import Author, Book


class FormAuthor(forms.ModelForm):
    
    class Meta:
        model = Author
        fields = ["first_name", "last_name"]



class FormBook(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = ["title", "page", 'author']
        
        
        