from django import forms
from ex_1.models import Author


class FormAuthor(forms.ModelForm):
    
    class Meta:
        model = Author
        fields = ["first_name", "last_name"]
