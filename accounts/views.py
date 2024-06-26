from django.shortcuts import render

# Create your views here.
# accounts/views.py
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import LoginForm, RegisterForm
from django.contrib.auth.views import LogoutView as DjangoLogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from core.models import Produto


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['imagens'] = Produto.objects.values_list('imagem', flat=True)
        produtos = Produto.objects.all()
        thumbs = [produto.imagem.thumb.url for produto in produtos]
        context['thumb_urls'] = thumbs
        context['first_thumb'] = thumbs[0]
        return context


    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, 'Invalid username or password')
            return self.form_invalid(form)


class LogoutView(DjangoLogoutView):
    next_page = reverse_lazy('login')


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = RegisterForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['imagens'] = Produto.objects.values_list('imagem', flat=True)
        produtos = Produto.objects.all()
        thumbs = [produto.imagem.thumb.url for produto in produtos]
        context['thumb_urls'] = thumbs
        context['first_thumb'] = thumbs[0]
        return context
        
    success_url = reverse_lazy('login')


