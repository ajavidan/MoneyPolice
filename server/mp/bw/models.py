from django.db import models

from datetime import datetime
# Create your models here.

class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2) #Negative amounts are used for spending
    payer = models.ForeignKey('bw.Payer')
    time = models.DateTimeField(default=datetime.now)
    fund = models.ForeignKey('bw.Fund', null=True)

class Fund(models.Model):
    name = models.CharField(max_length=25)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    budget = models.ForeignKey('bw.Budget')
    f_type = models.CharField(max_length=2) #saving fund or spending fund
    limit = models.DecimalField(max_digits=10, decimal_places=2)

    def __unicode__(self):
        return self.name

class Payer(models.Model):
    name = models.CharField(max_length=25)
    budget = models.ForeignKey('bw.Budget', null=True)
    # owner = models.ForeignKey('auth.User', related_name='payerss', on_delete=models.CASCADE)

class Budget(models.Model):
    # list of funds
    name = models.CharField(max_length=25)
    # owner = models.ForeignKey('auth.User', related_name='budgets', on_delete=models.CASCADE)

    def __unicode__(self):
        return '%s' % self.name
