# Generated by Django 4.1.5 on 2023-01-11 03:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sneakers', '0003_delete_worker'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bought',
            name='productBrand',
        ),
        migrations.RemoveField(
            model_name='bought',
            name='productImg',
        ),
        migrations.RemoveField(
            model_name='bought',
            name='productType',
        ),
    ]
