# Generated by Django 3.1.7 on 2021-03-06 01:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cashFlow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipe', models.CharField(choices=[('Credit', 'Credit'), ('Debit', 'Debit')], max_length=200)),
                ('desc', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.date.today)),
                ('priceCredit', models.FloatField(max_length=100)),
                ('priceDebit', models.FloatField(max_length=100)),
                ('priceSaldo', models.FloatField(max_length=100)),
            ],
        ),
    ]