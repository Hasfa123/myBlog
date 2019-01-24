from django import forms
from .models import Post, Comment
from PIL import Image

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('title', 'text','image',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)