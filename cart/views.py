from django.shortcuts import redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from core.models import Produto
from .cart import Cart
from .forms import CartAddProductForm
from django.http import JsonResponse,HttpResponse


class CartAddView(View):
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Produto, id=product_id)
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
            return JsonResponse({'success': True})
        print(form.errors, 'erro form')
        return JsonResponse({'success': False, 'error': 'O formulário não é válido'})

class CartRemoveView(View):
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Produto, id=product_id)
        cart.remove(product)
        # return JsonResponse({'success': True})
        # return HttpResponse(status=204)
        return redirect('index')

class CartDetailView(TemplateView):
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart(self.request)
        context['cart'] = cart
        return context

def empty_view_add(request):
    return HttpResponse('')
