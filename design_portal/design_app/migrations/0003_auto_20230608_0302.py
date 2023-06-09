# Generated by Django 3.2.16 on 2023-06-07 20:02

import design_app.utilities
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('design_app', '0002_category_request'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='request',
            name='design_img',
            field=models.ImageField(default='default_design.png', max_length=200, upload_to=design_app.utilities.get_timestamp_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])], verbose_name='Дизайн'),
        ),
        migrations.AlterField(
            model_name='request',
            name='author',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='request',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='design_app.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='request',
            name='description',
            field=models.TextField(max_length=1000, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='request',
            name='img',
            field=models.ImageField(default='empty_img.png', max_length=200, upload_to=design_app.utilities.get_timestamp_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])], verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.CharField(blank=True, choices=[('New', 'Новая'), ('Accepted for work', 'Принята в работу'), ('Completed', 'Выполнена')], default='New', max_length=20, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=200, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_username', message='Имя пользователя должно состоять только из латиницы, допускается дефис', regex='^[A-Za-z -]*$')], verbose_name='Login'),
        ),
    ]
