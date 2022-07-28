from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from app_menu.models import Entrada, Plato, Postre, Bebida, Contacto
from app_menu.forms import FormularioContacto
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate


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



# se creo la view contacto para el formulario web

def contacto (request):

    if request.method == "POST":

        contacto = FormularioContacto(request.POST)


        print(contacto)

        if contacto.is_valid:

            informacion = contacto.cleaned_data

            persona = Contacto( nombre = informacion ['nombre'], apellido = informacion ['apellido'], email = informacion['email'], telefono = informacion['telefono'])

            persona.save()

            return render ( request, "app_menu/exito.html")

    else:
        
        contacto  = FormularioContacto()

    return render (request, "app_menu/contacto.html", {"contacto": contacto})


#Se crea el Login

def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request,user)

                return render(request, "app_menu/inicio.html", {"mensaje": f"Bienvenido {usuario}"})

            else:

                return render(request, "app_menu/inicio.html", {"mensaje": "Error, datos incorrectos"})

        else:

                return render(request, "app_menu/inicio.html", {"mensaje": "Error, formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "app_menu/login.html", {'form': form})

#Se crea el Registro

def register(request):

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            form.save()
            return render(request, "app_menu/login.html", {"mensaje":"Usuario Creado"})
    
    else:
        form = UserCreationForm()

    return render(request,"app_menu/registro.html", {"form":"Usuario Creado"})   
