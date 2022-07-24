from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from app_menu.models import Entrada, Plato, Postre, Bebida


# Cree una vista de Inicio, para que al ir al Host nos lleve ahi

def Inicio ( request ):
    return render ( request, 'app_menu/inicio.html')


class EntradaList(ListView):
    queryset = Entrada.objects.all()
    template_name = "app_menu/entrada_list.html"
    context_object_name = "entradas"


class EntradaDetail(DetailView):
    model = Entrada
    template_name = "app_menu/entrada_detail.html"


class EntradaCreate (CreateView):
    model = Entrada
    fields = ['nombre', 'descripcion', 'precio', 'imagen', 'modificacion']
    template_name = "app_menu/entrada_form.html"
    success_url = reverse_lazy("entrada-list") 


class EntradaUpdate (UpdateView):
    model = Entrada
    fields = ['nombre', 'descripcion', 'precio', 'imagen', 'modificacion']
    success_url = reverse_lazy("entrada-list")


class EntradaDelete (DeleteView):
    model = Entrada
    success_url = reverse_lazy("entrada-list")


class PlatoList(ListView):
    queryset = Plato.objects.all()
    template_name = "app_menu/plato_list.html"
    context_object_name = "platos"


class PlatoDetail(DetailView):
    model = Plato
    template_name = "app_menu/plato_detail.html"


class PlatoCreate (CreateView):
    model = Plato
    fields = ['nombre', 'descripcion', 'precio', 'imagen', 'modificacion']
    template_name = "app_menu/plato_form.html"
    success_url = reverse_lazy("plato-list") 


class PlatoUpdate (UpdateView):
    model = Plato
    fields = ['nombre', 'descripcion', 'precio', 'imagen', 'modificacion']
    success_url = reverse_lazy("plato-list")


class PlatoDelete (DeleteView):
    model = Plato
    success_url = reverse_lazy("plato-list")


class PostreList(ListView):
    queryset = Postre.objects.all()
    template_name = "app_menu/postre_list.html"

    context_object_name = "postres"


class PostreDetail(DetailView):
    model = Postre
    template_name = "app_menu/postre_detail.html"


class PostreCreate (CreateView):
    model = Postre
    fields = ['nombre', 'descripcion', 'precio', 'imagen', 'modificacion']
    template_name = "app_menu/postre_form.html"
    success_url = reverse_lazy("postre-list") 


class PostreUpdate (UpdateView):
    model = Postre
    fields = ['nombre', 'descripcion', 'precio', 'imagen', 'modificacion']
    success_url = reverse_lazy("postre-list")


class PostreDelete (DeleteView):
    model = Postre
    success_url = reverse_lazy("postre-list")


class BebidaList(ListView):
    queryset = Bebida.objects.all()
    template_name = "app_menu/bebida_list.html"
    context_object_name = "bebidas"


class BebidaDetail(DetailView):
    model = Bebida
    template_name = "app_menu/bebida_detail.html"


class BebidaCreate (CreateView):
    model = Bebida
    fields = ['nombre', 'descripcion', 'precio', 'imagen', 'modificacion']
    template_name = "app_menu/bebida_form.html"
    success_url = reverse_lazy("bebida-list") 


class BebidaUpdate (UpdateView):
    model = Bebida
    fields = ['nombre', 'descripcion', 'precio', 'imagen', 'modificacion']
    success_url = reverse_lazy("bebida-list")


class BebidaDelete (DeleteView):
    model = Bebida
    success_url = reverse_lazy("bebida-list")