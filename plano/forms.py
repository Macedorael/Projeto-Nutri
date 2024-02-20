from django import forms
from .models import Paciente, Medida, Alimentos, Dietas, Refeicao, Circuferencias

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
                    'panturrilhadireita','panturrilhaesquerda','classificacao','rcq']


class AlimentoForm(forms.ModelForm):
    class Meta:
        model = Alimentos
        fields = ['nome', 'categoria']

class DietasForm(forms.ModelForm):
    class Meta:
        model = Dietas
        fields = ['refeicoes', 'quantidade', 'alimento']

class RefeicaoForm(forms.ModelForm):
    class Meta:
        model = Refeicao
        fields = ['id','refeicoes']