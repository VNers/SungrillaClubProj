# Generated by Django 5.0.6 on 2024-06-18 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sungrilla', '0019_remove_cart_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='portion_size',
            field=models.CharField(max_length=255),
        ),
    ]
