# Generated by Django 3.1.2 on 2020-10-20 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20201020_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addexpenses',
            name='tag',
            field=models.ManyToManyField(to='api.Tag'),
        ),
    ]
