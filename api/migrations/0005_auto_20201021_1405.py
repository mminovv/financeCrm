# Generated by Django 3.1.2 on 2020-10-21 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20201021_0121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addexpenses',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='addincome',
            name='slug',
        ),
    ]
