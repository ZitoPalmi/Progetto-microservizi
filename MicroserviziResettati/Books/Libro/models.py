from django.db import models

class Books(models.Model):
    Titolo = models.CharField(max_length=50)
    Autore = models.CharField(max_length=50)
    DAta_pubblicazione = models.DateTimeField('date published')
    Prezzo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.title) + " || " + str(self.author)
