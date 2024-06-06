from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.urls import reverse_lazy
from django.conf.urls.static import static
from .views import CartAddView, CartRemoveView, CartDetailView

app_name = 'cart'


urlpatterns = [
    path('', CartDetailView.as_view(), name='cart_detail'),
    path('add/<int:product_id>/', CartAddView.as_view(), name='cart_add'),
    path('remove/<int:product_id>/', CartRemoveView.as_view(), name='cart_remove'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)