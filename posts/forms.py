from django.forms import ModelForm
from .models import Post, Comment,Category
from django import forms

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'text1',
            'thumb',
            'text2',
            'img2',
            'categories'
        ]
        labels = {
            'title':"Título",
            'text1':"Primeiro bloco de texto:",
            'thumb':"Link da primeira imagem:",
            'text2':"Segundo bloco de texto:",
            'img2':"Link da segunda imagem:",
            'categories': "Selecione uma ou mais categorias:"
        }

        widgets = {
            'text1': forms.Textarea(attrs={'rows': 4, 'cols': 50}), 
            'text2': forms.Textarea(attrs={'rows': 4, 'cols': 50}),  
        }

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