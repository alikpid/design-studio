from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from .forms import RegisterUserForm
from django.urls import reverse_lazy
from .models import User


class Index(TemplateView):
    template_name = 'index.html'


class Register(CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('register-success')


class RegisterSuccess(TemplateView):
    template_name = 'register_ success.html'
