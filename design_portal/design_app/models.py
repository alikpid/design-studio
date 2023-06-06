from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


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
    username = models.CharField(max_length=200, verbose_name='Логин', unique=True, blank=False, validators=[
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