# Generated by Django 3.2.19 on 2023-06-13 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design_app', '0003_auto_20230608_0302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
    ]