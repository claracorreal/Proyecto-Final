from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, UpdateView
from app_menu.models import Entrada, Plato, Postre, Bebida, Contacto
from app_menu.forms import FormularioContacto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin

class Inicio (TemplateView):
    template_name = 'app_menu/inicio.html'


class About(TemplateView):
    template_name = 'app_menu/about.html'

# se creo la view contacto para el formulario web


def contacto (request):

    if request.method == "POST":

        contacto = FormularioContacto(request.POST)
        
        print(contacto)

        if contacto.is_valid:

            informacion = contacto.cleaned_data
            persona = Contacto( nombre = informacion ['nombre'], apellido = informacion ['apellido'],email = informacion['email'], telefono = informacion['telefono'])
            persona.save()
            return render ( request, "app_menu/exito.html")

    else:
        contacto  = FormularioContacto()
        
    return render (request, "app_menu/contacto.html", {"contacto": contacto})



@login_required
def dummy(request):
    render(request, "")


class EntradaInicio(ListView):
    queryset = Entrada.objects.all()
    template_name = "app_menu/entrada_inicio.html"
    context_object_name = "entradas"


class EntradaList(LoginRequiredMixin, ListView):
    queryset = Entrada.objects.all()
    template_name = "app_menu/entrada_list.html"
    context_object_name = "entradas"


class EntradaDetail(DetailView):
    model = Entrada
    template_name = "app_menu/entrada_detail.html"


class EntradaCreate (LoginRequiredMixin, CreateView):
    model = Entrada
    fields = ['nombre', 'descripcion', 'precio', 'imagen', 'modificacion']
    template_name = "app_menu/entrada_form.html"
    success_url = reverse_lazy("entrada-list") 


class EntradaUpdate (LoginRequiredMixin, UpdateView):
    model = Entrada
    fields = ['nombre', 'descripcion', 'precio', 'imagen', 'modificacion']
    success_url = reverse_lazy("entrada-list")


class EntradaDelete (LoginRequiredMixin, DeleteView):
    model = Entrada
    success_url = reverse_lazy("entrada-list")


class PlatoInicio(ListView):
    queryset = Plato.objects.all()
    template_name = "app_menu/plato_inicio.html"
    context_object_name = "platos"


class PlatoList(LoginRequiredMixin, ListView):
    queryset = Plato.objects.all()
    template_name = "app_menu/plato_list.html"
    context_object_name = "platos"


class PlatoDetail(DetailView):
    model = Plato
    template_name = "app_menu/plato_detail.html"


class PlatoCreate (LoginRequiredMixin, CreateView):
    model = Plato
    fields = ['nombre', 'descripcion', 'precio', 'imagen', 'modificacion']
    template_name = "app_menu/plato_form.html"
    success_url = reverse_lazy("plato-list") 


class PlatoUpdate (LoginRequiredMixin, UpdateView):
    model = Plato
    fields = ['nombre', 'descripcion', 'precio', 'imagen', 'modificacion']
    success_url = reverse_lazy("plato-list")


class PlatoDelete (LoginRequiredMixin, DeleteView):
    model = Plato
    success_url = reverse_lazy("plato-list")


class PostreInicio(ListView):
    queryset = Postre.objects.all()
    template_name = "app_menu/postre_inicio.html"
    context_object_name = "postres"


class PostreList(LoginRequiredMixin, ListView):
    queryset = Postre.objects.all()
    template_name = "app_menu/postre_list.html"
    context_object_name = "postres"


class PostreDetail(DetailView):
    model = Postre
    template_name = "app_menu/postre_detail.html"


class PostreCreate (LoginRequiredMixin, CreateView):
    model = Postre
    fields = ['nombre', 'descripcion', 'precio', 'imagen', 'modificacion']
    template_name = "app_menu/postre_form.html"
    success_url = reverse_lazy("postre-list") 


class PostreUpdate (LoginRequiredMixin, UpdateView):
    model = Postre
    fields = ['nombre', 'descripcion', 'precio', 'imagen', 'modificacion']
    success_url = reverse_lazy("postre-list")


class PostreDelete (LoginRequiredMixin, DeleteView):
    model = Postre
    success_url = reverse_lazy("postre-list")


class BebidaInicio(ListView):
    queryset = Bebida.objects.all()
    template_name = "app_menu/bebida_inicio.html"
    context_object_name = "bebidas"


class BebidaList(LoginRequiredMixin, ListView):
    queryset = Bebida.objects.all()
    template_name = "app_menu/bebida_list.html"
    context_object_name = "bebidas"


class BebidaDetail(DetailView):
    model = Bebida
    template_name = "app_menu/bebida_detail.html"


class BebidaCreate (LoginRequiredMixin, CreateView):
    model = Bebida
    fields = ['nombre', 'descripcion', 'precio', 'imagen', 'modificacion']
    template_name = "app_menu/bebida_form.html"
    success_url = reverse_lazy("bebida-list") 


class BebidaUpdate (LoginRequiredMixin, UpdateView):
    model = Bebida
    fields = ['nombre', 'descripcion', 'precio', 'imagen', 'modificacion']
    success_url = reverse_lazy("bebida-list")


class BebidaDelete (LoginRequiredMixin, DeleteView):
    model = Bebida
    success_url = reverse_lazy("bebida-list")



class EdicionMenu (LoginRequiredMixin, TemplateView):
    template_name= "app_menu/edicion_menu.html"

#Se crea el Login

class MenuLogin(LoginView):
    template_name = 'app_menu/login.html'
    next_page = reverse_lazy("edicion-menu")



class MenuLogout(LogoutView):
    template_name = 'app_menu/logout.html'



class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'app_menu/registro.html'
    success_url = reverse_lazy('menu-login')
    form_class = UserCreationForm
    success_message = "¡¡Se creo tu perfil satisfactoriamente!!"
  


class UserProfile(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = User
    template_name = "app_menu/user_detail.html"
    
    def test_func(self):
        return self.request.user.id == int(self.kwargs['pk'])


class UserUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = User
    template_name = "app_menu/user_form.html"
    fields = ["email", "first_name", "last_name", "username"]

    def get_success_url(self):
        return reverse_lazy("user-detail", kwargs={"pk": self.request.user.id})
    
    def test_func(self):
        return self.request.user.id == int(self.kwargs['pk'])
    