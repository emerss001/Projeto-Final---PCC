# Generated by Django 4.0.3 on 2022-07-09 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_remove_cliente_datapagamento'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='pagamento',
            field=models.CharField(blank=True, max_length=19),
        ),
    ]
