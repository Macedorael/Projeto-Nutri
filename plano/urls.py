from django.urls import path
from .views import login,planos, logout, cadastro, painel,paciente,criar_plano,plano,imc,fazermedida,antropometria,circuferencias,fazercircuferencia,pacientes

urlpatterns = [
    path('', login , name='login'),
    path('logout/', logout , name='logout'),
    path('cadastro/',cadastro, name='cadastro'),
    path('painel/', painel, name = 'painel'),
    path('pacientes/<int:pk>/', pacientes, name='pacientes'),
    path('paciente/<int:pk>', paciente, name='paciente'),
    path('plano/<int:plano_id>', plano, name='plano'),
    path('antropometria/<int:pk>', antropometria, name='antropometria'),
    path('imc/<int:pk>', imc, name='imc'),
    path('circuferencias/<int:pk>', circuferencias, name='circuferencias'),
    path('fazermedida/<int:pk>', fazermedida, name='fazermedida'),
    path('fazercircuferencia/<int:pk>', fazercircuferencia, name='fazercircuferencia'),
    path('planos/<int:pk>', planos, name='planos'),
    path('criar_plano/<int:pk>/', criar_plano, name='criar_plano')
    

]