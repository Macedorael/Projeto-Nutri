from django.contrib import admin
from .models import Paciente, Alimentos, Medida, Dietas,Refeicao,Circuferencias,Categorias,Gorduras


class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome','telefone','email','nascimento','criado','modificado','ativo','genero')

class MedidaAdmin(admin.ModelAdmin):
    list_display = ('nome','peso','altura','imc','classificacao','criado')

class CircuferenciasAdmin(admin.ModelAdmin):
    list_display = ('nome','pescoco','ombro','torax','bracodireito','bracoesquerdo','bracodireitocontraido','bracoesquerdocontraido','antebracodireito','antebracoesquerdo',
                    'cintura','abdome','quadril','coxadistaldireita','coxadistalesquerda','coxamedialdireita','coxamedialesquerda','coxaproximaldireita','coxaproximalesquerda',
                    'panturrilhadireita','panturrilhaesquerda','classificacao','rcq','criado')


class AlimentoAdmin(admin.ModelAdmin):
    list_display = ('nome','categoria','umidade','energiakcal','energiakj','proteina','lipideos','colesterol','carboidrato','fibraalimentar',
                    'cinzas','calcio','magnesio','manganes','fosforo','ferro','sodio','potassio','cobre','zinco','retinol','tiamina','riboflavina',
                    'piridoxina','niacina','vitaminac')


class DietasAdmin(admin.ModelAdmin):
    list_display = ('refeicoes','paciente','quantidade','alimento', 'criado')

class RefeicaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'refeicoes')


class ValorenegeticosAdmin(admin.ModelAdmin):
    list_display = ('alimento','nutriente','valor')

class CategoriasAdmin(admin.ModelAdmin):
    list_display = ['nome']

class GordurasAdmin(admin.ModelAdmin):
    list_display = ('nome','saturados','monoinsaturados','poliinsaturados')



admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Medida, MedidaAdmin)
admin.site.register(Alimentos, AlimentoAdmin)
admin.site.register(Dietas, DietasAdmin)
admin.site.register(Refeicao, RefeicaoAdmin)
admin.site.register(Circuferencias, CircuferenciasAdmin)
admin.site.register(Categorias, CategoriasAdmin)
admin.site.register(Gorduras, GordurasAdmin)