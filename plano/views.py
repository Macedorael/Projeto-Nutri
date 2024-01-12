from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

from .bdo import PacienteService
from .forms import PacienteForm, AlimentoForm, DietasForm,MedidaForm,CircuferenciasForm
from .models import Paciente, Alimento,Medida,Dietas,Refeicao,Circuferencias
from django.contrib import messages
from django.db.models import  Q
from django.utils.dateparse import parse_date
from django.urls import reverse
from datetime import date



def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            return redirect('painel') 
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    logout(request)
    return redirect('login')


def cadastro(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)  
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('cadastro')
        else:
            messages.error(request, 'Erro ao cadastrar!')
    else:
        form = PacienteForm()
    
    return render(request, 'cadastro_paciente.html', {'form': form})


def painel(request):
    pacientes = Paciente.objects.all()
    context={
        'pacientes': pacientes
    }
    return render(request, 'painel.html',context)



def plano(request, pk):
    paciente_form = Paciente.objects.get(id=pk)
    paciente = Paciente.objects.get(id=pk)
    data_especifica = None
    data_especifica_frm = None

    if request.method == 'POST':
        try:
            data_especifica = request.POST.get('data_especifica')
            data_especifica_frm = parse_date(data_especifica)
        except:
            pass

        form = DietasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('plano', pk=pk) 
    else:
        form = DietasForm(initial={'paciente': paciente})

    objPacienteService = PacienteService()
    retDietaPaciente = objPacienteService.get_dietas_by_paciente_and_data(paciente, data_especifica_frm)
    retSomaProteinas = objPacienteService.get_soma_proteinas(retDietaPaciente)

    context = {
        'paciente_form': paciente_form,
        'form': form,
        'paciente': paciente,
        'data_filtro' : data_especifica
    }
    context.update(retDietaPaciente)
    context.update(retSomaProteinas)
    
    return render(request, 'plano.html', context)


def paciente(request, pk):
    paciente = Paciente.objects.get(id=pk)
    medida = Medida.objects.filter(id=pk)
    data_nascimento = paciente.nascimento
    
    data_atual = date.today()
    idade = data_atual.year - data_nascimento.year - ((data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day))

    context = {
        'paciente': paciente,
        'medida': medida,
        'idade' : idade,
        
    }
    return render(request, 'paciente.html',context)

def antropometria(request,pk):
    paciente = Paciente.objects.get(id=pk)
    context = {
        'paciente': paciente,
        
    }
    return render(request, 'antropometria.html',context)
    

def imc(request, pk):
    paciente = Paciente.objects.get(id=pk)
    medidas = Medida.objects.filter(nome=paciente)
    context = {
        'paciente': paciente,
        'medidas': medidas,
    }
    return render(request, 'imc.html', context)

def circuferencias(request, pk):
    paciente = Paciente.objects.get(id=pk)
    circuferencias = Circuferencias.objects.filter(nome=paciente)
    context = {
        'paciente': paciente,
        'circuferencias': circuferencias
    }

    return render(request, 'circuferencias.html', context)



def fazermedida(request,pk):
    paciente = Paciente.objects.get(id=pk)

    if request.method == 'POST':
        nome = paciente
        peso = float(request.POST.get('peso'))
        altura = float(request.POST.get('altura'))
        
        imc = peso / (altura * altura )
        

        if imc < 18.5:
            classificacao = 'DESNUTRIÇÃO'
        
        elif imc >= 18.5 and imc <= 24.9:
            classificacao = 'EUTRÓFICO'
        
        elif imc >= 25.0 and imc <= 29.9:
            classificacao = 'SOBREPESO'

        elif imc >= 30.0 and imc < 34.9:
            classificacao = 'OBESIDADE GRAU 1'

        elif imc >= 35.0 and imc < 39.9:
            classificacao = 'OBESIDADE GRAU 2'

        else:
            classificacao ='OBESIDADE GRAU 3'

            
        medida = Medida(nome=nome,peso=peso, altura=altura, imc=imc, classificacao=classificacao)
        medida.save()

        
        return redirect('imc', pk=pk)
    context={
        'paciente': paciente

    }
    return render(request, 'fazermedida.html',context)

def fazercircuferencia(request,pk):
    paciente = Paciente.objects.get(id=pk)

    if request.method == 'POST':

        nome = paciente
        pescoco = float(request.POST.get('pescoco'))
        ombro = float(request.POST.get('ombro'))
        torax = float(request.POST.get('torax'))
        bracodireito = float(request.POST.get('bracodireito'))
        bracoesquerdo = float(request.POST.get('bracoesquerdo'))
        bracodireitocontraido = float(request.POST.get('bracodireitocontraido'))
        bracoesquerdocontraido = float(request.POST.get('bracoesquerdocontraido'))
        antebracodireito = float(request.POST.get('antebracodireito'))
        antebracoesquerdo = float(request.POST.get('antebracoesquerdo'))
        cintura = float(request.POST.get('cintura'))
        abdome = float(request.POST.get('abdome'))
        quadril = float(request.POST.get('quadril'))
        coxadistaldireita = float(request.POST.get('coxadistaldireita'))
        coxadistalesquerda = float(request.POST.get('coxadistalesquerda'))
        coxamedialdireita = float(request.POST.get('coxamedialdireita'))
        coxamedialesquerda = float(request.POST.get('coxamedialesquerda'))
        coxaproximaldireita = float(request.POST.get('coxaproximaldireita'))
        coxaproximalesquerda = float(request.POST.get('coxaproximalesquerda'))
        panturrilhadireita = float(request.POST.get('panturrilhadireita'))
        panturrilhaesquerda = float(request.POST.get('panturrilhaesquerda'))

        rcq = cintura / quadril
        data_nascimento = paciente.nascimento
        data_atual = date.today()
        idade = data_atual.year - data_nascimento.year - ((data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day))
        

        if paciente.genero == 'Masculino':

            if idade <= 29:
                if rcq < 0.83:
                    classificacao = 'Baixo'
                elif rcq < 0.88:
                    classificacao = 'Moderado'
                elif rcq < 0.94:
                    classificacao = 'Alto'
                elif rcq > 0.94:
                    classificacao = 'Muito Alto'

            elif idade <= 39:
                if rcq < 0.84:
                    classificacao = 'Baixo'
                elif rcq < 0.91:
                    classificacao = 'Moderado'
                elif rcq < 0.96:
                    classificacao = 'Alto'
                elif rcq > 0.96:
                    classificacao = 'Muito Alto'

            elif idade <= 49:
                if rcq < 0.88:
                    classificacao = 'Baixo'
                elif rcq < 0.95:
                    classificacao = 'Moderado'
                elif rcq < 0.100:
                    classificacao = 'Alto'
                elif rcq > 0.100:
                    classificacao = 'Muito Alto'

            elif idade <= 59:
                if rcq < 0.90:
                    classificacao = 'Baixo'
                elif rcq < 0.96:
                    classificacao = 'Moderado'
                elif rcq < 0.102:
                    classificacao = 'Alto'
                elif rcq > 0.102:
                    classificacao = 'Muito Alto'

            elif idade > 59:
                if rcq < 0.91:
                    classificacao = 'Baixo'
                elif rcq < 0.98:
                    classificacao = 'Moderado'
                elif rcq < 0.103:
                    classificacao = 'Alto'
                elif rcq > 0.103:
                    classificacao = 'Muito Alto'

        elif paciente.genero == 'Feminino':

            if idade <= 29:
                if rcq < 0.71:
                    classificacao = 'Baixo'
                elif rcq < 0.77:
                    classificacao = 'Moderado'
                elif rcq < 0.82:
                    classificacao = 'Alto'
                elif rcq > 0.82:
                    classificacao = 'Muito Alto'

            elif idade <= 39:
                if rcq < 0.72:
                    classificacao = 'Baixo'
                elif rcq < 0.78:
                    classificacao = 'Moderado'
                elif rcq < 0.84:
                    classificacao = 'Alto'
                elif rcq > 0.84:
                    classificacao = 'Muito Alto'

            elif idade <= 49:
                if rcq < 0.73:
                    classificacao = 'Baixo'
                elif rcq < 0.79:
                    classificacao = 'Moderado'
                elif rcq < 0.87:
                    classificacao = 'Alto'
                elif rcq > 0.87:
                    classificacao = 'Muito Alto'

            elif idade <= 59:
                if rcq < 0.74:
                    classificacao = 'Baixo'
                elif rcq < 0.81:
                    classificacao = 'Moderado'
                elif rcq < 0.88:
                    classificacao = 'Alto'
                elif rcq > 0.88:
                    classificacao = 'Muito Alto'

            elif idade > 59:
                if rcq < 0.76:
                    classificacao = 'Baixo'
                elif rcq < 0.83:
                    classificacao = 'Moderado'
                elif rcq < 0.90:
                    classificacao = 'Alto'
                elif rcq > 0.90:
                    classificacao = 'Muito Alto'



        circuferencias = Circuferencias(nome=nome,pescoco=pescoco, ombro= ombro,torax=torax, bracodireito=bracodireito, bracoesquerdo=bracoesquerdo,  bracodireitocontraido= bracodireitocontraido,
        bracoesquerdocontraido=bracoesquerdocontraido, antebracodireito= antebracodireito, antebracoesquerdo=antebracoesquerdo, 
        cintura=cintura, abdome=abdome, quadril=quadril, coxadistaldireita=coxadistaldireita, coxadistalesquerda=coxadistalesquerda, 
        coxamedialdireita=coxamedialdireita, coxamedialesquerda=coxamedialesquerda, coxaproximaldireita=coxaproximaldireita,
        coxaproximalesquerda=coxaproximalesquerda, panturrilhadireita=panturrilhadireita, panturrilhaesquerda=panturrilhaesquerda,
        classificacao=classificacao)

        circuferencias.save()

        
        return redirect('circuferencias',pk=pk)
    context={
        'paciente': paciente

    }
    return render(request, 'fazercircuferencias.html',context)