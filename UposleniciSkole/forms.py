from django import forms
from .models import Uposlenik, Ucenik

class UposlenikForm(forms.ModelForm):
    class Meta:
        model = Uposlenik
        fields = ["ime", "prezime", "pozicija", "godine_rada", "pravo_na_godisnji",]

class UcenikForm(forms.ModelForm):
    class Meta:
        model = Ucenik
        fields = ["ime", "prezime", "godiste"]
