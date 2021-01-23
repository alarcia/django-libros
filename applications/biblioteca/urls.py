from django.urls import path, re_path

from . import views

app_name="biblioteca_app"

urlpatterns = [
    path('autores', views.ListaAutores.as_view(), name="lista-autores")
]
