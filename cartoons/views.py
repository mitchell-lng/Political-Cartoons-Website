from django.shortcuts import render

from .models import Cartoon


def frontend(request):
    data = {
        'cartoons': Cartoon.objects.all()
    }

    return render(request, 'cartoons/main.html', data)
