from django.forms import ModelForm
from .models import Post,Comment


class PostCreationForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title","body"] 

class CommentCreationForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]