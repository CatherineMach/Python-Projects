# Generated by Django 2.2.5 on 2023-07-06 23:26

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UniversityCampus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=60)),
                ('state', models.TextField(blank=True, max_length='2')),
                ('campusID', models.IntegerField(blank=True, default='')),
            ],
            options={
                'verbose_name_plural': 'University Campus',
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]