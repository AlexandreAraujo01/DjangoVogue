from django.shortcuts import render
from django.views.generic import TemplateView,View
from .models import Produto
import math
from django.http import HttpResponse
from django.core.serializers import serialize
import json
from django.http import JsonResponse

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
        context['produtos_json'] = produtos_json = serialize('json', produtos)
        context['parcelas'] = parcelas
        return context


class CategoryFilterView(TemplateView):
    template_name = "index.html"
    
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
        parcelas = []
        for produto in produtos:
            if produto.preco <= 300:
                parcelas.append(f"2x de {math.ceil(produto.preco / 2)}")
            else:
                parcelas.append(f"4x de {math.ceil(produto.preco / 4)}")
        context['produtos'] = produtos
        context['parcelas'] = parcelas
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
<<<<<<< HEAD
=======


class ApplyFilterView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            filtro_escolhido = data.get("filtro_chave", "preco")  
            url_type = data.get("url_type", None)

            dic_categorias = {
            "CAMISA": 1, "JEANS": 2, "VESTIDO": 3,
            "SHORT": 4, "CASACO": 5, "ACESSORIOS": 6, "OUTROS": 7
        }

            print(url_type,'url_type')
            if url_type:
                categoria_int = dic_categorias.get(url_type.upper())
                produtos1 = Produto.objects.filter(categoria=categoria_int)
                produtos = produtos1.order_by(f"{filtro_escolhido}")
                imagens = [f'{produto.imagem.thumb.url}' for produto in produtos]
                produtos = list(produtos.values())
                print(produtos, 'lele')
            else:
                produtos = list(Produto.objects.order_by(f"{filtro_escolhido}").values())
                imagens = [f'{produto.imagem.thumb.url}' for produto in Produto.objects.order_by(f"{filtro_escolhido}")]
                
            parcelas = []
            for index,produto in enumerate(produtos):
                produto["imagem"] = imagens[index]
                if produto['preco'] <= 300:
                    parcelas.append(f"2x de {math.ceil(produto['preco'] / 2)}")
                else:
                    parcelas.append(f"4x de {math.ceil(produto['preco'] / 4)}")

            return JsonResponse({'success': True, 'produtos': produtos, 'parcelas': parcelas})
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Invalid JSON'}, status=400)
>>>>>>> retomando_projeto
    



<<<<<<< HEAD

=======
>>>>>>> retomando_projeto
# Create your views here.