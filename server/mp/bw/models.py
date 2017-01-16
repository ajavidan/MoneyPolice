from django.db import models

# Create your models here.

class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=25)
    t_type = models.BooleanField()
    payer = models.CharField(max_length=15)
    time = models.DateTimeField()
