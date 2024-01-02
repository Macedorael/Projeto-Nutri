from django.urls import path
from .views import login, logout, cadastro, painel,paciente,plano,imc,fazermedida,antropometria,circuferencias

urlpatterns = [
    path('', login , name='login'),
    path('logout/', logout , name='logout'),
    path('cadastro/',cadastro, name='cadastro'),
    path('painel/', painel, name = 'painel'),
    path('paciente/<int:pk>', paciente, name='paciente'),
    path('plano/<int:pk>', plano, name='plano'),
    path('antropometria/<int:pk>', antropometria, name='antropometria'),
    path('imc/<int:pk>', imc, name='imc'),
    path('circuferencias/<int:pk>', circuferencias, name='circuferencias'),
    path('fazermedida/<int:pk>', fazermedida, name='fazermedida'),
    

]