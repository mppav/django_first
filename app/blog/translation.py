from modeltranslation.translator import translator, register, TranslationOptions
from .models import Post


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

# translator.register(Post, PostTranslationOptions)