from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.core.validators import FileExtensionValidator
from .utilities import get_timestamp_path


class User(AbstractUser):
    surname = models.CharField(max_length=200, verbose_name='Фамилия', blank=False, validators=[
        RegexValidator(
            regex='^[А-Яа-я -]*$',
            message='Фамилия пользователя должна состоять из кириллицы, допускается дефис',
            code='invalid_surname'
        ),
    ])
    name = models.CharField(max_length=200, verbose_name='Имя', blank=False, validators=[
        RegexValidator(
            regex='^[А-Яа-я -]*$',
            message='Имя пользователя должно состоять из кириллицы, допускается дефис',
            code='invalid_name'
        ),
    ])
    middlename = models.CharField(max_length=200, verbose_name='Отчество', blank=True, validators=[
        RegexValidator(
            regex='^[А-Яа-я -]*$',
            message='Отчество пользователя должно состоять из кириллицы, допускается пробел',
            code='invalid_middlename'
        ),
    ])
    username = models.CharField(max_length=200, verbose_name='Login', unique=True, blank=False, validators=[
        RegexValidator(
            regex='^[A-Za-z -]*$',
            message='Имя пользователя должно состоять только из латиницы, допускается дефис',
            code='invalid_username'
        ),
    ])
    email = models.EmailField(max_length=200, verbose_name='Почта', blank=False)
    user_agreement = models.BooleanField(default=False,
                                         help_text='Прочел и ознакомлен с <a href="http://www.sfmolga.ru/agreement.pdf'
                                                   '">Пользовательским соглашением</a>')


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Request(models.Model):
    day_add = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, verbose_name='Название', blank=False)
    description = models.TextField(max_length=1000, verbose_name="Описание", blank=False)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE, blank=False)
    author = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE, blank=True, default=None)
    img = models.ImageField(max_length=200, verbose_name="Изображение", default="empty_img.png", upload_to=get_timestamp_path, blank=False,
                            validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])
    design_img = models.ImageField(max_length=200, default="default_design.png", blank=False, verbose_name="Дизайн" , upload_to=get_timestamp_path,
                                   validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])

    STATUS_CHOICES = [
        ('New', 'Новая'),
        ('Accepted for work', 'Принята в работу'),
        ('Completed', 'Выполнена'),
    ]
    status = models.CharField(max_length=20, verbose_name="Статус", choices=STATUS_CHOICES, blank=True, default='New')

    def get_status_name(self):
        for status in self.STATUS_CHOICES:
            if status[0] == self.status:
                return status[1]
        return 'Не задан'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-day_add']
