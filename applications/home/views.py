from django.shortcuts import render

from django.views.generic import(
    TemplateView,
    ListView,
)

class IndexView(TemplateView):
    template_name = "home/index.html"

class ListaLibros(ListView):
    template_name = "home/lista.html"
    queryset = ['El Quijote', 'Código limpio', 'La sombra del viento', 'Django 2.0']
    context_object_name = 'libros'
