# Generated by Django 3.1.7 on 2021-03-09 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0005_auto_20210306_1038'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cashflow',
            old_name='saldo',
            new_name='saldoCredit',
        ),
        migrations.AddField(
            model_name='cashflow',
            name='saldoDebit',
            field=models.FloatField(default=0, max_length=100),
        ),
    ]