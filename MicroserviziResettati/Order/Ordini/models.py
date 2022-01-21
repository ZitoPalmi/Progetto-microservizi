from django.db import models

# Create your models here.
class Order(models.Model):
    id_book = models.IntegerField(blank=False)
    id_customer = models.IntegerField(blank=False)

class Meta:
    ordering = ['id']