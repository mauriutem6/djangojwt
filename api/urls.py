
from django.contrib import admin
from django.urls import path
from .views import get_usuario


urlpatterns=[
    path('get_usuario/', get_usuario.as_view()),
]