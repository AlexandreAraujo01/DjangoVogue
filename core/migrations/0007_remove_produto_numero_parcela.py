# Generated by Django 4.2.13 on 2024-05-23 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_produto_numero_parcela'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='numero_parcela',
        ),
    ]