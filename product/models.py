from django.db import models
from django.urls import reverse


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    inStock = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_id': self.pk})

    class Meta:
        ordering = ['name', 'price', 'inStock']
