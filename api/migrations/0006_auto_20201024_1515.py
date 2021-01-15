# Generated by Django 3.1.2 on 2020-10-24 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20201021_1405'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('account_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_from', to='api.bankaccount')),
                ('account_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_to', to='api.bankaccount')),
            ],
        ),
        migrations.RemoveField(
            model_name='checkexpenses',
            name='expenses',
        ),
        migrations.RemoveField(
            model_name='checkincome',
            name='income',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.DeleteModel(
            name='CheckExpenses',
        ),
        migrations.DeleteModel(
            name='CheckIncome',
        ),
    ]
