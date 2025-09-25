from django.urls import path
from . import views

urlpatterns = [
    path("uposlenici/", views.lista_objekata, {"tip": "uposlenici"}, name="lista_uposlenika"),
    path("ucenici/", views.lista_objekata, {"tip": "ucenici"}, name="lista_ucenika"),
    path("uposlenici/dodaj/", views.dodaj_uposlenika, name="dodaj_uposlenika"),
    path("uposlenici/obrisi/<int:pk>/", views.obrisi_uposlenika, name="obrisi_uposlenika"),
]