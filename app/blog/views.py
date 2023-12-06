from django.shortcuts import render
from datetime import datetime

from django.http import HttpResponse

def index(reguest):
    # return HttpResponse("<h1>Hello</h1>")
    context = {'data': datetime.now(),
               'asd':123}

    return render(reguest, "index.html", context)