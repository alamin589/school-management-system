# Generated by Django 4.1.5 on 2024-01-01 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='current_class',
        ),
    ]
