
from django.contrib import admin
from django.urls import path
from .views import get_usuario, get_usuarios


urlpatterns=[
    path('get_usuario/', get_usuario.as_view()),
    path('get_usuarios/', get_usuarios.as_view()),
]