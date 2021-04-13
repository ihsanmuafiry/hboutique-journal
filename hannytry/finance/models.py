from django.db import models
import datetime

# Create your models here.

class cashFlow(models.Model):
    def __str__(self):
        return self.desc

    TIPE = (
        ('Credit', 'Credit'),
        ('Debit', 'Debit'),)

    tipe = models.CharField(max_length=200, choices=TIPE)
    date = models.DateField(default=datetime.date.today)
    price = models.FloatField(max_length=100, default=0)
    desc = models.TextField(max_length=200)


    saldoCredit = models.FloatField(max_length=100,default=0)
    saldoDebit = models.FloatField(max_length=100, default=0)






