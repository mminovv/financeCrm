# Generated by Django 3.1.2 on 2020-11-30 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20201130_2015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contractor',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='contractor',
            name='is_deleted',
        ),
    ]