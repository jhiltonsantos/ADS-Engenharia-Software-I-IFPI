# Generated by Django 2.2.7 on 2020-01-13 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20191216_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='data_final',
            field=models.DateTimeField(null=True, verbose_name='DataFinal'),
        ),
        migrations.AddField(
            model_name='evento',
            name='data_inicial',
            field=models.DateTimeField(null=True, verbose_name='DataInicial'),
        ),
    ]
