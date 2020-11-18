from django import forms
from .models import Author


class UserForms(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'password', 'author_alias', 'email')
