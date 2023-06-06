from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from .forms import RegisterUserForm, RequestForm
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
    user = request.user
    applications = Request.objects.filter(author=user)
    has_applications = applications.exists()

    context = {
        'applications': applications,
        'has_applications': has_applications,
    }

    return render(request, 'profile.html', context)


def create_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST, request.FILES)
        if form.is_valid():
            request_obj = form.save(commit=False)
            request_obj.author = request.user
            request_obj.save()
            return redirect('profile')
    else:
        form = RequestForm()
    return render(request, 'create_request.html', {'form': form})

