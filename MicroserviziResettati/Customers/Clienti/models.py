from django.db import models

# Create your models here.
# Create your models here.
from django.db import models

class Customers(models.Model):
    Nome = models.CharField(max_length=50)
    Cognome = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    Dta_di_nascita = models.DateTimeField('date published')

    def __str__(self):
        return str(self.name) + str(self.surname)