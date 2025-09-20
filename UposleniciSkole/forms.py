from django import forms
from .models import Uposlenik

class UposlenikForm(forms.ModelForm):
    class Meta:
        model = Uposlenik
        fields = ["ime", "prezime", "pozicija", "godine_rada", "pravo_na_godisnji",]
