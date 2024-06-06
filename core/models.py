from django.db import models
from stdimage.models import StdImageField

#SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify
import math

# Create your models here.

class Base(models.Model):
    criado = models.DateTimeField('Data de Criacao', auto_now_add=True)
    modificado = models.DateTimeField('Data de Atualizacao', auto_now_add=True)
    ativo = models.BooleanField("Ativo?", default=True)

    class Meta:
        abstract = True


class Produto(Base):
    CAMISA = 1
    JEANS = 2
    VESTIDO = 3
    SHORT = 4
    CASACO = 5
    ACESSORIOS = 6
    OUTROS = 7

    CATEGORIA_OPCOES = [
        (CAMISA, 'Camisa'),
        (JEANS, 'Jeans'),
        (VESTIDO, 'Vestido'),
        (SHORT, "Short"),
        (CASACO, "Casaco"),
        (ACESSORIOS, "Acessorios"),
        (OUTROS, "Outros")
    ]

    nome = models.CharField("Nome",max_length=100)
    preco = models.DecimalField("Preco", max_digits=8, decimal_places=2)
    estoque = models.IntegerField("Estoque")
    imagem = StdImageField('imagem',upload_to="produtos", variations={"thumb": (350,350)})
    slug = models.SlugField('slug', max_length=100,blank=True, editable=False)
    categoria = models.IntegerField(choices=CATEGORIA_OPCOES, default=OUTROS)
    parcela = models.DecimalField("Parcela", max_digits=8, decimal_places=2, blank=True, null=True)
    numero_parcela = models.IntegerField("Numero Parcela", blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.parcela:  # Se a parcela ainda não foi definida
            # Calcula a parcela como metade do preço do produto
            self.parcela = math.ceil(self.preco) / 2 if self.preco < 300 else math.ceil(self.preco) / 4
            self.numero_parcela = 2 if self.preco < 300 else 4
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome


def produto_pre_save(signal, instance, sender, **kargs):
    instance.slug = slugify(instance.nome)


signals.pre_save.connect(produto_pre_save, sender=Produto)



