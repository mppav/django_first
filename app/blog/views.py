from django.shortcuts import render, get_object_or_404
from datetime import datetime
from django.utils.translation import gettext as _
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .models import Category, Post
from .forms import SearchForm, SimplePostForm, PostForm

class MenuMixin:

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


class Index(MenuMixin, TemplateView):
    template_name = "index_cbv.html"

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        posts = Post.objects.all()
        context["posts"] = posts
        return context

class PostList(MenuMixin, ListView):
    model = Post
    paginate_by = 2

class PostDetail(MenuMixin, DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class PostCreateView(MenuMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'category']
    success_url = "/"

def index(request):
    # return HttpResponse("<h1>Hello</h1>")
    # print(reguest.GET.get('q'))

    categories = Category.objects.all()
    # q = request.GET.get('q')
    search_form = SearchForm(request.GET)
    # print(search_form)
    # if q is not None:
    if search_form.is_valid() and search_form.cleaned_data['q']:
        posts = Post.objects.filter(title__icontains=search_form.cleaned_data['q'])
    else:
        posts = Post.objects.all()
    context = {
        "posts": posts,
        "categories": categories,
        'data': datetime.now(),
        'asd': _("Text to translate"),
        "form": search_form,
    }

    return render(request, "index.html", context)





def by_category(request, **kwargs):
    pk = kwargs.get("pk")
    # print(pk)
    # category = Category.objects.get(pk=pk)
    category = get_object_or_404(Category, pk=pk)
    categories = Category.objects.all()
    context = {
        "category": category,
        "categories": categories,
    }
    return render(request, "category.html", context)


def post_add(request):
    categories = Category.objects.all()
    form = SimplePostForm()
    context = {
        "categories": categories,
        'form': form,
    }
    return render(request, "post_create.html", context)


def post_save(request):
    categories = Category.objects.all()
    if request.method == "POST":
        form = SimplePostForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            post = Post(title=form.cleaned_data['title'], content=form.cleaned_data['content'],
                        category=Category.objects.all().first())
            post.save()
            return HttpResponseRedirect('/')
    context = {
        "categories": categories,
        'form': form,
    }
    return render(request, "post_create.html", context)



def post_create(request):
    categories = Category.objects.all()
    context = {
        "categories": categories,
    }
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return  HttpResponseRedirect('/')
        else:
            context['form'] = form
    else:
        form = PostForm()

    context['form'] = form
    return render(request, "post_create.html", context)