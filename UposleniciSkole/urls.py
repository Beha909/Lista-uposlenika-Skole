from django.urls import path
from . import views

app_name = "UposleniciSkole"

urlpatterns = [
    path("uposlenici/dodaj/", views.dodaj_uposlenika, name="dodaj_uposlenika"),
    path("uposlenici/obrisi/<int:pk>/", views.obrisi_uposlenika, name="obrisi_uposlenika"),
    path("ucenici/dodaj/", views.dodaj_ucenika, name="dodaj_ucenika"),

    path("list-view/<str:model_name>/", views.lista_objekata, name="lista_objekata"),         # LISTA OBJEKATA
]

 
