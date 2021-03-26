from django.shortcuts import render

from .models import Cartoon, Draft


def frontend(request, slug=None, term=None):
    data = {
        'cartoons': Cartoon.objects.all(),
    }

    return render(request, 'cartoons/main.html', data)
