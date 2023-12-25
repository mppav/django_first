"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from blog.views import index, by_category, post_add, post_save, post_create
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings


urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
    # path("", index),
    # path('admin/', admin.site.urls),
]

urlpatterns += i18n_patterns(
    path("", index, name="index"),

    path("post/add/", post_add, name="post_add"),
    path("post/save/", post_save, name="post_save"),

    path("post/create/", post_create, name="post_create"),

    path("category/<int:pk>/", by_category, name="by_category"),
    path('admin/', admin.site.urls),
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]
