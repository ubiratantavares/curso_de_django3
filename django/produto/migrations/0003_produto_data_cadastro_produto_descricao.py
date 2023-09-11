# Generated by Django 4.0.2 on 2023-01-08 09:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_alter_produto_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='data_cadastro',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='produto',
            name='descricao',
            field=models.CharField(default='', max_length=100),
        ),
    ]
