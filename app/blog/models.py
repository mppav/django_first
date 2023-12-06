from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=250, verbose_name=_("Category title"))

    class Meta:
        ordering = ["title"]


class Post(models.Model):
    title = models.CharField(max_length=250, verbose_name=_("Post title"))
    content = models.TextField(verbose_name=_("Post content"))
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT)

    class Meta:
        verbose_name = _("Blog post")
        verbose_name_plural = _("Blog posts")

    def __str__(self):
        return f"{self.title} - {self.content[:50]}"
