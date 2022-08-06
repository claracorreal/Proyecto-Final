
from django import views
from django.urls import path
from .views import (EntradaList, EntradaInicio, EntradaDetail, EntradaCreate, EntradaUpdate, EntradaDelete, MenuLogin, MenuLogout,
                            PlatoList, PlatoInicio, PlatoDetail, PlatoCreate, PlatoUpdate, PlatoDelete,
                            PostreList, PostreInicio, PostreDetail, PostreCreate, PostreUpdate, PostreDelete,
                            BebidaList, BebidaInicio, BebidaDetail, BebidaCreate, BebidaUpdate, BebidaDelete,
                            Inicio,About,contacto, MenuLogin ,SignUpView, UserUpdate, EdicionMenu, UserProfile, dummy)

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', Inicio.as_view(), name='inicio'),
    path('about', About.as_view(), name='about'),
    path('contacto/',contacto,name='contacto'),
    path('entrada/list/', EntradaList.as_view(), name='entrada-list'),
    path('entrada/inicio/', EntradaInicio.as_view(), name='entrada-inicio'),
    path('entrada/<pk>/', EntradaDetail.as_view(), name='entrada-detail'),
    path('entrada/create',EntradaCreate.as_view(), name='entrada-create'),
    path('entrada/<pk>/update', EntradaUpdate.as_view(), name='entrada-update'),
    path('entrada/<pk>/delete', EntradaDelete.as_view(), name='entrada-delete'),
    path('plato/list/', PlatoList.as_view(), name='plato-list'),
    path('plato/inicio/', PlatoInicio.as_view(), name='plato-inicio'),
    path('plato/<pk>/', PlatoDetail.as_view(), name='plato-detail'),
    path('plato/create',PlatoCreate.as_view(), name='plato-create'),
    path('plato/<pk>/update', PlatoUpdate.as_view(), name='plato-update'),
    path('plato/<pk>/delete', PlatoDelete.as_view(), name='plato-delete'),
    path('postre/list/', PostreList.as_view(), name='postre-list'),
    path('postre/inicio/', PostreInicio.as_view(), name='postre-inicio'),
    path('postre/<pk>/', PostreDetail.as_view(), name='postre-detail'),
    path('postre/create',PostreCreate.as_view(), name='postre-create'),
    path('postre/<pk>/update', PostreUpdate.as_view(), name='postre-update'),
    path('postre/<pk>/delete', PostreDelete.as_view(), name='postre-delete'),
    path('bebida/list/', BebidaList.as_view(), name='bebida-list'),
    path('bebida/inicio/', BebidaInicio.as_view(), name='bebida-inicio'),
    path('bebida/<pk>/', BebidaDetail.as_view(), name='bebida-detail'),
    path('bebida/create',BebidaCreate.as_view(), name='bebida-create'),
    path('bebida/<pk>/update', BebidaUpdate.as_view(), name='bebida-update'),
    path('bebida/<pk>/delete', BebidaDelete.as_view(), name='bebida-delete'),
    path('login/', MenuLogin.as_view(), name = 'menu-login'),
    path("registro/", SignUpView.as_view(), name="menu-registro"),
    path('logout', MenuLogout.as_view(), name= 'menu-logout'),
    path('dummy', dummy, name="dummy"),
    path("user/<pk>", UserProfile.as_view(), name="user-detail"),
    path("user/<pk>/edit", UserUpdate.as_view(), name="user-update"),
    path('edicion/', EdicionMenu.as_view(), name='edicion-menu'),

]