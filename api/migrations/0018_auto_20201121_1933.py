# Generated by Django 3.1.2 on 2020-11-21 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20201120_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='description',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
