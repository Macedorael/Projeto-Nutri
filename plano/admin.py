from django.contrib import admin
from .models import Paciente, Alimento, Medida, Dietas,Refeicao,Circuferencias


class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome','telefone','email','nascimento','criado','modificado','ativo',)

class MedidaAdmin(admin.ModelAdmin):
    list_display = ('nome','peso','altura','imc','classificacao','criado')

class CircuferenciasAdmin(admin.ModelAdmin):
    list_display = ('nome','pescoco','ombro','torax','bracodireito','bracoesquerdo','bracodireitocontraido','bracoesquerdocontraido','antebracodireito','antebracoesquerdo',
                    'cintura','abdome','quadril','coxadistaldireita','coxadistalesquerda','coxamedialdireita','coxamedialesquerda','coxaproximaldireita','coxaproximalesquerda',
                    'panturrilhadireita','panturrilhaesquerda','classificacao','criado')


class AlimentoAdmin(admin.ModelAdmin):
    list_display = ('nome','peso', 'proteina', 'modificado')


class DietasAdmin(admin.ModelAdmin):
    list_display = ('refeicoes','paciente','quantidade', 'alimento', 'criado')

class RefeicaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'refeicoes',) 


admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Medida, MedidaAdmin)
admin.site.register(Alimento, AlimentoAdmin)
admin.site.register(Dietas, DietasAdmin)
admin.site.register(Refeicao, RefeicaoAdmin)
admin.site.register(Circuferencias, CircuferenciasAdmin)