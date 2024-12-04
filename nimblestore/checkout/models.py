from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, default=None)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name
