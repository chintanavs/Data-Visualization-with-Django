from django.db import models


class Order(models.Model):
    bank_name = models.CharField(max_length=20)
    transaction_status = models.CharField(max_length=50)
    total_log = models.DecimalField(max_digits=5, decimal_places=2)
    kpi = models.DecimalField(max_digits=5, decimal_places=2)
