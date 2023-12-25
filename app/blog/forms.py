from django.forms import Form, CharField, ModelForm
from .models import Post


class SearchForm(Form):
    q = CharField(max_length=10, required=False, label="Search", help_text='Search post by title')

class SimplePostForm(Form):
    title = CharField(max_length=250, label="title")
    content = CharField(label="content")


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content', 'category']