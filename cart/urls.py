from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.urls import reverse_lazy
from django.conf.urls.static import static
from .views import CartAddView, CartRemoveView, CartDetailView, CartProductsView, CartSubtractView

app_name = 'cart'


urlpatterns = [
    path('', CartDetailView.as_view(), name='cart_detail'),
    path('show/', CartProductsView.as_view(), name="cart_show"),
    path('add/', CartAddView.as_view(), name='cart_add'),
    path('subtract/', CartSubtractView.as_view(), name='cart_subtract'),
    path('remove/<int:product_id>/', CartRemoveView.as_view(), name='cart_remove'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)