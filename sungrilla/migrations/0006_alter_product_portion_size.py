# Generated by Django 5.0.6 on 2024-06-16 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sungrilla', '0005_alter_product_portion_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='portion_size',
            field=models.CharField(max_length=50),
        ),
    ]
