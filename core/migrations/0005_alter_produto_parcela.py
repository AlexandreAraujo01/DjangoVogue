# Generated by Django 4.2.13 on 2024-05-23 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_produto_parcela_alter_produto_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='parcela',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Parcela'),
        ),
    ]
