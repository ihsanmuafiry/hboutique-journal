# Generated by Django 3.1.7 on 2021-03-06 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_auto_20210306_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashflow',
            name='desc',
            field=models.TextField(max_length=200),
        ),
    ]