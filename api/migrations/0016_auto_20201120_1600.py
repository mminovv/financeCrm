# Generated by Django 3.1.2 on 2020-11-20 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateField(),
        ),
    ]