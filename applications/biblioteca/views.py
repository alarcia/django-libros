from django.shortcuts import render

from django.views.generic import(
    TemplateView,
    ListView,
    CreateView,
)

from .models import Autor, Libros


class ListaAutores(ListView):
    template_name = "biblioteca/lista-autores.html"
    model = Autor
    context_object_name = 'autores'

class ListaLibrosAutores(ListView):
    template_name = "biblioteca/lista-libros.html"
    context_object_name = 'libros'

    def get_queryset(self):
        # identificar el autor
        id = self.kwargs['pk']
        # filtro de los Libros
        lista = Libros.objects.filter(
            autor=id
        )

        # devuelvo el resultado o la lista
        return lista

class AddAutor(CreateView):
    template_name = "biblioteca/add-autor.html"
    model = Autor
    fields = ['nombre', 'nacionalidad',]
    success_url = '/'
