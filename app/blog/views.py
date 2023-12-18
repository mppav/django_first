from django.shortcuts import render
from datetime import datetime
from django.utils.translation import gettext as _
from django.http import HttpResponse

def index(reguest):
    # return HttpResponse("<h1>Hello</h1>")
    context = {'data': datetime.now(),
               'asd': _("Text to translate")}

    return render(reguest, "index.html", context)