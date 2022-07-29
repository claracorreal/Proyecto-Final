
from django import views
from django.urls import path
from .forms import FormularioContacto
from .views import (EntradaList, EntradaDetail, EntradaCreate, EntradaUpdate, EntradaDelete,
                            PlatoList, PlatoDetail, PlatoCreate, PlatoUpdate, PlatoDelete,
                            PostreList, PostreDetail, PostreCreate, PostreUpdate, PostreDelete,
                            BebidaList, BebidaDetail, BebidaCreate, BebidaUpdate, BebidaDelete,
                            Inicio, contacto, login_request,SignUpView, UserUpdate)

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('entrada/list/', EntradaList.as_view(), name='entrada-list'),
    path('entrada/<pk>/', EntradaDetail.as_view(), name='entrada-detail'),
    path('entrada/create',EntradaCreate.as_view(), name='entrada-create'),
    path('entrada/<pk>/update', EntradaUpdate.as_view(), name='entrada-update'),
    path('entrada/<pk>/delete', EntradaDelete.as_view(), name='entrada-delete'),
    path('plato/list/', PlatoList.as_view(), name='plato-list'),
    path('plato/<pk>/', PlatoDetail.as_view(), name='plato-detail'),
    path('plato/create',PlatoCreate.as_view(), name='plato-create'),
    path('plato/<pk>/update', PlatoUpdate.as_view(), name='plato-update'),
    path('plato/<pk>/delete', PlatoDelete.as_view(), name='plato-delete'),
    path('postre/list/', PostreList.as_view(), name='postre-list'),
    path('postre/<pk>/', PostreDetail.as_view(), name='postre-detail'),
    path('postre/create',PostreCreate.as_view(), name='postre-create'),
    path('postre/<pk>/update', PostreUpdate.as_view(), name='postre-update'),
    path('postre/<pk>/delete', PostreDelete.as_view(), name='postre-delete'),
    path('bebida/list/', BebidaList.as_view(), name='bebida-list'),
    path('bebida/<pk>/', BebidaDetail.as_view(), name='bebida-detail'),
    path('bebida/create',BebidaCreate.as_view(), name='bebida-create'),
    path('bebida/<pk>/update', BebidaUpdate.as_view(), name='bebida-update'),
    path('bebida/<pk>/delete', BebidaDelete.as_view(), name='bebida-delete'),
    path('', Inicio, name='inicio'),
    path('contacto/',contacto,name='contacto'),
    path('login', login_request, name = 'Login'),
    path("registro/", SignUpView.as_view(), name="registro"),
    path('logout', LogoutView.as_view(template_name='app_menu/logout.html'), name= 'Logout'),
    path("user/<pk>/edit", UserUpdate.as_view(), name="user-update"),

]