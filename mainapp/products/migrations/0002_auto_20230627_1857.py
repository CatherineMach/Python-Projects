# Generated by Django 2.2.5 on 2023-06-27 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('appetizers', 'appetizers'), ('treats', 'treats'), ('entrees', 'entrees'), ('drinks', 'drinks')], max_length=60),
        ),
    ]
