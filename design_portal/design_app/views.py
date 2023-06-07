from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.http import HttpResponseBadRequest
from .forms import RegisterUserForm, RequestForm, CategoryForm
from .models import User, Request, Category
from .utilities import is_admin


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
    if user.is_superuser:
        applications = Request.objects.all()
        has_applications = applications.exists()
    else:
        applications = Request.objects.filter(author=user)
        has_applications = applications.exists()

    context = {
        'applications': applications,
        'has_applications': has_applications,
    }

    return render(request, 'profile.html', context)


@login_required
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


@login_required
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


@login_required
@user_passes_test(is_admin)
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_manager.html', {'categories': categories})


@login_required
@user_passes_test(is_admin)
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_manager')
    else:
        form = CategoryForm()

    return render(request, 'add_category.html', {'form': form})


@login_required
@user_passes_test(is_admin)
def delete_category(request, request_id):
    category = get_object_or_404(Category, id=request_id)
    if request.method == 'GET':
        return render(request, 'category_delete.html', {'category': category})

    if request.method == 'POST':
        category.delete()
        return redirect('category_manager')

    return render(request, 'category_manager.html', {'category': category})


@login_required
@user_passes_test(is_admin)
def change_status(request, request_id):
    request_obj = get_object_or_404(Request, id=request_id)
    if request_obj.status == 'New':
        if request.method == 'POST':
            design_image = request.FILES.get('design_image')
            new_status = request.POST.get('status')
            comment = request.POST.get('comment')

            if new_status == 'Completed' and design_image:
                request_obj.design_img = design_image
                request_obj.status = 'Completed'
                request_obj.save()
                messages.success(request, 'Статус заявки успешно изменен на "Выполнено"')
            elif new_status == 'Accepted for work' and comment:
                request_obj.status = 'Accepted for work'
                request_obj.save()
                messages.success(request, 'Статус заявки успешно изменен на "Принято в работу"')
            else:
                messages.error(request, 'Некорректный новый статус или отсутствует необходимый параметр')

            return redirect('profile')

    else:
        messages.error(request, 'Смена статуса с текущего статуса невозможна')

    return render(request, 'change_status.html', {'request_obj': request_obj})