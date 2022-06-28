from django.db import models


class Order(models.Model):
    number = models.BigIntegerField(blank=True, null=True)
    dol_price = models.BigIntegerField(blank=True, null=True)
    rub_price = models.BigIntegerField(blank=True, null=True)
    delivery_time = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.id)