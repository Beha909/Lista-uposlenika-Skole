from django.db import models

# Create your models here.

class Uposlenik(models.Model):
    ime = models.CharField(max_length= 100)
    prezime = models.CharField(max_length= 100)
    pozicija = models.CharField(max_length= 100)
    godine_rada = models.IntegerField()
    pravo_na_godisnji = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.ime} {self.prezime}"