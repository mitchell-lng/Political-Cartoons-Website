from django.urls import path

from .views import frontend

urlpatterns = [
    path('', frontend, name='frontend'),
    path('about', frontend, name='frontend'),
    path('cartoon/<slug:slug>', frontend, name='frontend'),
    path('search/', frontend, name='frontend'),
    path('search/<str:term>', frontend, name='frontend'),
    path('search/author/<str:term>', frontend, name='frontend'),
]
