from django.db import models
from django.utils import timezone
timezone.now
from django.db.models import  Q


class Base(models.Model):
    criado = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True )

    class Meta:
        abstract = True

class Paciente(Base):
    nome = models.CharField('nome', max_length=100)
    telefone = models.CharField('Telefone', max_length=20)
    email = models.EmailField('E-mail')
    nascimento = models.DateField('Data de Nascimento')
    genero = models.CharField('Genero', max_length=100)
    

    def __str__(self):
        return self.nome
 

class Medida(Base):
    nome = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    peso = models.DecimalField('Peso', max_digits=15, decimal_places=2)
    altura = models.DecimalField('Altura', max_digits=15, decimal_places=2)
    imc = models.DecimalField('Imc', max_digits=15,decimal_places=3)
    classificacao = models.CharField('Classificação', max_length=20)
    
    def __str__(self) -> str:
        return f'{self.nome}'
    
class Circuferencias(Base):
    nome = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    pescoco = models.DecimalField('Pescoço', max_digits=15, decimal_places=2)
    ombro = models.DecimalField('Ombro', max_digits=15, decimal_places=2)
    torax = models.DecimalField('Torax', max_digits=15, decimal_places=2)
    bracodireito = models.DecimalField('Braçodireito', max_digits=15, decimal_places=2)
    bracoesquerdo = models.DecimalField('Braçoesquerdo', max_digits=15, decimal_places=2)
    bracodireitocontraido = models.DecimalField('Braçodireitocontraido', max_digits=15, decimal_places=2)
    bracoesquerdocontraido = models.DecimalField('Braçoesquerdocontraido', max_digits=15, decimal_places=2)
    antebracodireito = models.DecimalField('Antebraçodireito', max_digits=15, decimal_places=2)
    antebracoesquerdo = models.DecimalField('Antebraçoesquerdo', max_digits=15, decimal_places=2)
    cintura = models.DecimalField('Cintura', max_digits=15, decimal_places=2)
    abdome = models.DecimalField('Abdome', max_digits=15, decimal_places=2)
    quadril = models.DecimalField('Quadril', max_digits=15, decimal_places=2)
    coxadistaldireita = models.DecimalField('Coxadistaldireita', max_digits=15, decimal_places=2)
    coxadistalesquerda = models.DecimalField('Coxadistalesquerda ', max_digits=15, decimal_places=2)
    coxamedialdireita = models.DecimalField('Coxamedialdireita', max_digits=15, decimal_places=2)
    coxamedialesquerda = models.DecimalField('Coxamedialesquerda', max_digits=15, decimal_places=2)
    coxaproximaldireita = models.DecimalField('Coxaproximaldireita', max_digits=15, decimal_places=2)
    coxaproximalesquerda = models.DecimalField('Coxaproximalesquerda', max_digits=15, decimal_places=2)
    panturrilhadireita = models.DecimalField('Panturrilhadireita', max_digits=15, decimal_places=2)
    panturrilhaesquerda = models.DecimalField('Panturrilhaesquerda', max_digits=15, decimal_places=2)
    classificacao = models.CharField('Classificação', max_length=20)
    rcq = models.DecimalField('Rcq', max_digits=15, decimal_places=2)

    def __str__(self) -> str:
        return self.nome.nome
    
class Categorias(models.Model):
    nome = models.CharField('Nome', max_length=100)

    def __str__(self) -> str:
        return self.nome
        

class Alimentos(models.Model):
    nome = models.CharField('Nome', max_length=100)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    umidade = models.FloatField('Umidade')
    energiakcal = models.FloatField('Energia kcal')
    energiakj = models.FloatField('Energia kj')
    proteina = models.FloatField('Proteína')
    lipideos = models.FloatField('Lipídeos')
    colesterol = models.FloatField('Colesterol')
    carboidrato = models.FloatField('Carboidrato')
    fibraalimentar = models.FloatField('Fibra Alimentar')
    cinzas = models.FloatField('Cinzas')
    calcio = models.FloatField('Cálcio')
    magnesio = models.FloatField('Magnésio')
    manganes = models.FloatField('Manganês')
    fosforo = models.FloatField('Fósforo ')
    ferro = models.FloatField('Ferro')
    sodio = models.FloatField('Sódio')
    potassio = models.FloatField('Potássio')
    cobre = models.FloatField('Cobre')
    zinco = models.FloatField('Zinco')
    retinol = models.FloatField('Retinol')
    tiamina = models.FloatField('Tiamina')
    riboflavina = models.FloatField('Riboflavina')
    piridoxina = models.FloatField('Piridoxina')
    niacina = models.FloatField('Niacina')
    vitaminac = models.FloatField('Vitamina C')
    
    
    

    def __str__(self) -> str:
        return self.nome
    

class Refeicao(Base):
    refeicoes = models.CharField('Refeições',max_length=30)

    def __str__(self) -> str:
        return f'{self.refeicoes}'
    

class Dietas(Base):
    refeicoes = models.ForeignKey(Refeicao, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    quantidade = models.IntegerField('Quantidade')
    alimento = models.ForeignKey(Alimentos, on_delete=models.CASCADE)

        
    def __str__(self) -> str:
        return f'{self.refeicoes}'


