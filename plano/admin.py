from django.contrib import admin
from .models import Paciente, Alimentos, Medida, Dietas,Refeicao,Circuferencias,Categorias,Gorduras,PlanoAlimentar


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

    def get_plano(self, obj):
        return obj.plano.nome
    get_plano.short_description = 'Plano Alimentar'

    def get_criacao_plano(self, obj):
        return obj.plano.criado
    get_criacao_plano.short_description = 'Criação Plano Alimentar'

    def get_paciente(self, obj):
        return obj.plano.paciente.nome
    get_paciente.short_description = 'Paciente'

    list_display = ('get_plano','get_criacao_plano','get_paciente','refeicoes','quantidade','alimento', 'criado')

class RefeicaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'refeicoes')

class ValorenegeticosAdmin(admin.ModelAdmin):
    list_display = ('alimento','nutriente','valor')

class CategoriasAdmin(admin.ModelAdmin):
    list_display = ['nome']

class GordurasAdmin(admin.ModelAdmin):
    list_display = ('nome','saturados','monoinsaturados','poliinsaturados')

class PlanoAlimentarAdmin(admin.ModelAdmin):
    list_display = ('id','nome','paciente','criado')


admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Medida, MedidaAdmin)
admin.site.register(Alimentos, AlimentoAdmin)
admin.site.register(PlanoAlimentar, PlanoAlimentarAdmin)
admin.site.register(Dietas, DietasAdmin)
admin.site.register(Refeicao, RefeicaoAdmin)
admin.site.register(Circuferencias, CircuferenciasAdmin)
admin.site.register(Categorias, CategoriasAdmin)
admin.site.register(Gorduras, GordurasAdmin)