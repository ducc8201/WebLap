# Generated by Django 3.1.3 on 2020-11-29 03:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0001_initial'),
        ('Checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Orderdetail',
            new_name='Order_Product',
        ),
    ]
