from django.contrib import admin
from .models import Post, Category

# Register your models here.
admin.site.register(Category)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content', 'published')


admin.site.register(Post, PostAdmin)