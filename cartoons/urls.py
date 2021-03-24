from django.urls import path

from .views import frontend

urlpatterns = [
    path('', frontend, name='frontend'),
    path('cartoon/<slug:slug>', frontend, name='frontend'),
]
