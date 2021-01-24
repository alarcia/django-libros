from django.urls import path, re_path

from . import views

app_name="home_app"

urlpatterns = [
    path('libros', views.ListaLibros.as_view(), name="lista")
]
