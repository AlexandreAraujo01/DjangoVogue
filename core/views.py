from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Produto
import math
from django.http import HttpResponse

class IndexView(TemplateView):
    template_name = "index.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        produtos = Produto.objects.all()
        parcelas = []
        for produto in produtos:
            if produto.preco <= 300:
                parcelas.append(f"2x de {math.ceil(produto.preco / 2)}")
            else:
                parcelas.append(f"4x de {math.ceil(produto.preco / 4)}")
        context['produtos'] = produtos
        context['parcelas'] = parcelas
        return context

class CategoryFilterView(TemplateView):
    template_name = "categoria.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        nome_categoria = self.kwargs.get('nome_categoria').upper()
        dic_categorias = {
            "CAMISA": 1, "JEANS": 2, "VESTIDO": 3,
            "SHORT": 4, "CASACO": 5, "ACESSORIOS": 6, "OUTROS": 7
        }
        categoria_int = dic_categorias.get(nome_categoria)
        
        if categoria_int is None:
            # Adicione um tratamento para categorias inválidas, como redirecionar para uma página de erro
            raise Http404(f"Categoria '{nome_categoria}' não encontrada.")
        
        produtos = Produto.objects.filter(categoria=categoria_int)
        context['produtos'] = produtos
        return context




class TesteView(TemplateView):
    template_name = "index2.html"
    def get_context_data(self, **kwargs):
        numeros = [1, 2, 3, 4, 5]
        context = super().get_context_data(**kwargs)
        context['numeros'] = numeros
        return context


class SearchFilterView(TemplateView):
    template_name = "filtro.html"
    def get_context_data(self, **kwargs) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        nome_pesquisa = self.kwargs.get("nome_pesquisa")
        if nome_pesquisa == "":
            produtos = Produto.objects.all()
        else:
            produtos = Produto.objects.filter(nome__icontains=nome_pesquisa)
        context["produtos"] = produtos
        return context
    




# Create your views here.