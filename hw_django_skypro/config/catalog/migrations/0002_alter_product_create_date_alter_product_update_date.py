# Generated by Django 4.2.7 on 2023-12-03 13:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='create_date',
            field=models.DateField(default=datetime.date(2023, 12, 3), verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='update_date',
            field=models.DateField(default=datetime.date(2023, 12, 3), verbose_name='Дата последнего изменения'),
        ),
    ]
