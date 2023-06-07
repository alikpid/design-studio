from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from .forms import RegisterUserForm, RequestForm
from django.urls import reverse_lazy
from .models import User, Request
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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


def delete_request(request, request_id):
    request_obj = get_object_or_404(Request, id=request_id)

    if request.method == 'GET':
        return render(request, 'delete_request.html', {'request_obj': request_obj})

    if request.method == 'POST':
        if request.user.is_authenticated and request.user == request_obj.author:
            if request_obj.status not in ['Accepted for work', 'Completed']:
                request_obj.delete()
                messages.success(request, 'Заявка успешно удалена')
                return redirect('profile')
            else:
                messages.error(request, 'Нельзя удалить заявку со статусом "Принято в работу" или "Выполнено"')
        else:
            messages.error(request, 'У вас нет прав для удаления этой заявки')

    return redirect('profile')
