# Generated by Django 4.2.10 on 2024-03-03 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dataInventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categorias',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dataInventory.categoria'),
            preserve_default=False,
        ),
    ]
