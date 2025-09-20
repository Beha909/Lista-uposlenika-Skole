from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_uposlenika, name="lista_uposlenika"),
    path("dodaj/", views.dodaj_uposlenika, name="dodaj_uposlenika"),
    path("obrisi/<int:pk>/", views.obrisi_uposlenika, name="obrisi_uposlenika"),
]