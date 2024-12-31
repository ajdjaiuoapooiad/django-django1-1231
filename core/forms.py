

from django import forms

from core.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields= ['user','text']
        