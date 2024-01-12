from django import forms
from .models import Paciente, Medida, Alimento, Dietas, Refeicao, Circuferencias

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'telefone', 'email','nascimento','genero']

class MedidaForm(forms.ModelForm):
    class Meta:
        model = Medida
        fields = ['nome', 'peso', 'altura','imc','classificacao']

class CircuferenciasForm(forms.ModelForm):
    class Meta:
        model = Circuferencias
        fields = ['nome','pescoco','ombro','torax','bracodireito','bracoesquerdo','bracodireitocontraido','bracoesquerdocontraido','antebracodireito','antebracoesquerdo',
                    'cintura','abdome','quadril','coxadistaldireita','coxadistalesquerda','coxamedialdireita','coxamedialesquerda','coxaproximaldireita','coxaproximalesquerda',
                    'panturrilhadireita','panturrilhaesquerda','classificacao']


class AlimentoForm(forms.ModelForm):
    class Meta:
        model = Alimento
        fields = ['nome', 'peso', 'proteina']

class DietasForm(forms.ModelForm):
    class Meta:
        model = Dietas
        fields = ['refeicoes','paciente', 'quantidade', 'alimento']

class RefeicaoForm(forms.ModelForm):
    class Meta:
        model = Refeicao
        fields = ['id','refeicoes']