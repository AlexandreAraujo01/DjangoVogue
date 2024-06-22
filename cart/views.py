from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from django.http import JsonResponse
from core.models import Produto
from .cart import Cart

class CartAddView(View):
    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))
        update_quantity = request.POST.get('update_quantity', 'false') == 'true'

        if product_id:
            try:
                product = Produto.objects.get(id=product_id)
                cart = Cart(request)
                cart.add(product=product, quantity=quantity, update_quantity=update_quantity)
                return JsonResponse({'success': True, 'message': 'Produto adicionado ao carrinho', 'cart': cart.cart})
            except Produto.DoesNotExist:
                return JsonResponse({'success': False, 'message': 'Produto não encontrado'})
        return JsonResponse({'success': False, 'message': 'ID do produto não fornecido'})


class CartSubtractView(View):
    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))
        update_quantity = request.POST.get('update_quantity', 'false') == 'true'

        if product_id:
            try:
                product = Produto.objects.get(id=product_id)
                cart = Cart(request)
                cart.decrement(product=product, quantity=quantity, update_quantity=update_quantity)
                return JsonResponse({'success': True, 'message': 'Produto decrementado ao carrinho', 'cart': cart.cart})
            except Produto.DoesNotExist:
                return JsonResponse({'success': False, 'message': 'Produto não encontrado'})
        return JsonResponse({'success': False, 'message': 'ID do produto não fornecido'})

class CartRemoveView(View):
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Produto, id=product_id)
        cart.remove(product)
        return JsonResponse({'success': True, 'cart': cart.cart})

class CartDetailView(TemplateView):
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart(self.request)
        context['cart'] = cart
        return context


class CartProductsView(View):

    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        cart_items = []
        for item in cart:
            cart_items.append({
                'product_id': item['product'].id,
                'name': item['product'].nome,
                'quantity': item['quantity'],
                'price': str(item['price']),
                'total_price': str(item['total_price']),
                'product_image': str(item['product'].imagem.thumb.url),
            })
        final_price =  str(sum([float(item['total_price']) for item in cart_items]))

        return JsonResponse({'success': True, 'cart': cart_items, 'final_price': final_price, "items_number": len(cart)})
    
 
