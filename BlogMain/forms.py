from django import forms
from .models import *


class CustomAdmin(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 7, 'cols': 100}))

    class Meta:
        model = Post
        fields = ["timestamp", "author", "title", "text", "img"]
