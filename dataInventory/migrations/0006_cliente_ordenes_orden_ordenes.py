# Generated by Django 4.2.10 on 2024-03-04 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataInventory', '0005_remove_product_categorias_product_categorias'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='ordenes',
            field=models.ManyToManyField(to='dataInventory.orden'),
        ),
        migrations.AddField(
            model_name='orden',
            name='ordenes',
            field=models.ManyToManyField(to='dataInventory.product'),
        ),
    ]