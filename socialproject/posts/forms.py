from .models import Posts, Comment
from django import forms

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('title','image','caption')

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields = ('body','posted_by')