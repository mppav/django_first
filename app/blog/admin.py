from django.contrib import admin
from .models import Post, Category
from modeltranslation.admin import TranslationAdmin
# Register your models here.
admin.site.register(Category)


# # class PostAdmin(admin.ModelAdmin):
class PostAdmin(TranslationAdmin):
    pass
    # list_display = ('title', 'content')
#     list_display_links = ('title', 'content')
#     search_fields = ('title', 'content', 'published')
#
#
admin.site.register(Post, PostAdmin)
