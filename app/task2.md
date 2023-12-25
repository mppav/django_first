# t2

## Migrations

manage.py makemigrations
manage.py migrate

## Models

create()
save()
редагування
delete()

Manager
    all()
    get()
    order_by()
    filter()

## Templates

теги
    {% %}
    for
дерективи (вивід змінних)
    {{ p.published }}
фільтри
   {{ p.published|date : "d.m.Y H:i:s" }}  
генерація шаблону
    from django.http import HttpResponse
    from django.template import loader
    from .models import Post
    def index (request):
        template = loader.get_template('bboard/index.html')
        posts = Post.objects.order_by('-published')
        context = {"posts" : posts }
        return HttpResponse(template.render(context, request))
        
    return render(request, 'bboard/index.html', {'posts' : posts })
    
## Admin site

manage.py createsuperuser

admin.site.register(Post)

## Model fields properties

verbose_name_plural
verbose_name
ordering

class PostAdmin (admin.ModelAdmin):
    list_display = ('title', 'content')
    list_display_links = ('title', 'content' )
    search_fields = ('title', 'content', 'published')
    
admin.site.register(Post, PostAdmin)

=================

# Models

## Models connection

ForeignKey
    PROTECTED
    CASCAED
    
## URL параметри

category/<int:pk>/ - category/10/

сторінка з поточною категорією публікацій в переліком всіх постів

## Зворотнє перетворення адрес за його name

path('category/<int:pk>/' , category , name='category'),

<а href="category/{{ category.pk }}/"> - <a href="{% url 'category' category.pk %}">

## Html форми

<form action="" method="get" class="form-example">
  <div class="form-example">
    <label for="name">Search: </label>
    <input type="text" name="q" id="search" required />
  </div>
<div class="form-example">
    <input type="submit" value="Search" />
  </div>
</form>

## Модельні форми

from django.forms import ModelForm

class PostForm (ModelForm) :
    class Meta :
        model = Post
        fields ('title', 'content')
        
## Класова в'юха на основі CreateView

<form method="post">
{% csrf_token %}
{{ fomn.as_p }}
<input type="submit" vаluе="Створити" >
</form>


## Наслідування шаблонів
{% extends "base.html" %}
{% include "menu.html" %}


urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

STATIC_ROOT = BASE_DIR / 'staticfiles' 
STATIC_URL = '/static/'

# Forms

my_form.cleaned_data['field']

response: GET, POST, FILES, method, scheme, path, path_info, content_type, content_params, МЕТА, body, resolver_match

HttpResponseRedirect

my_form(initial={"title": "Post title"})
my_form(instance=...)


# Models

## Загальні параметри для всіх типів полів
verbose_name
help_text
default
unique
unique_for_date
unique_for_month
unique_for_year
null
blank
db_index
editable
db_column

## Типи полів
 
CharField