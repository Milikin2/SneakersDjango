# Generated by Django 4.1.4 on 2022-12-12 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sneakers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productPrice',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена'),
        ),
    ]
