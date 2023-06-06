from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from .forms import RegisterUserForm
from django.urls import reverse_lazy
from .models import User, Request
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class Index(TemplateView):
    template_name = 'index.html'


class Register(CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('register-success')


class RegisterSuccess(TemplateView):
    template_name = 'register_ success.html'


class Login(LoginView):
    template_name = 'login.html'


class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'logout.html'


@login_required
def profile(request):
    reqs = Request.objects.filter(author=request.user.pk)
    context = {'reqs': reqs}
    return render(request, 'profile.html', context)
