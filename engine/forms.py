from django import forms
from engine.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'