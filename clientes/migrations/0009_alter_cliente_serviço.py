# Generated by Django 4.0.3 on 2022-07-10 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('serviços', '0001_initial'),
        ('clientes', '0008_cliente_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='Serviço',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='serviços.serviço'),
        ),
    ]
