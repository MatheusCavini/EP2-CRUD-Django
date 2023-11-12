from django.forms import ModelForm
from .models import Post, Comment
from django import forms

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [
            'author',
            'text',
        ]
        labels = {
            'author': 'Usuário',
            'text': 'Escreva seu comentário',
        }
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'cols': 50})  
        }