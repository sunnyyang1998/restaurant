# Generated by Django 4.2 on 2023-05-14 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_remove_order_products'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
