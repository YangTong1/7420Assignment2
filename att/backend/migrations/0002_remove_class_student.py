# Generated by Django 4.0.4 on 2023-11-14 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='student',
        ),
    ]
