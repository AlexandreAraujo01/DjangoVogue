from django.contrib import admin
from django.urls import path
from .views import IndexView, TesteView, CategoryFilterView, SearchFilterView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('teste/', TesteView.as_view(), name="teste"), 
    path('categoria/<str:nome_categoria>/',CategoryFilterView.as_view(), name="categoria"),
    path('pesquisa/<str:nome_pesquisa>/', SearchFilterView.as_view(), name= "filtroPesquisa")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
