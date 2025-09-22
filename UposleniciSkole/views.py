from django.shortcuts import render, redirect, get_object_or_404
from .models import Uposlenik
from .forms import UposlenikForm
from django.core.paginator import Paginator




# Create your views here.

'''
Funkcija:

Uzmi sve modele.
Procesiraj onaj model koji je user zatrazio, modeli mogu biti uposlenik ili ucenik
Uzmi iz modela sva imena varijabli
To saljes na frontend (imena kolona)
Uzmi iz modela vrijednosti iz tih varijabli
Saljes i to, loadas na frontendu

'''





def lista_uposlenika(request):
    uposlenici = Uposlenik.objects.all().order_by("id")
    paginator = Paginator(uposlenici, 10)  
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "radnici/lista_uposlenika.html", {"page_obj": page_obj})      # Ako ne bude funkcionisalo, requesta stavi templates



'''
Dodaj objekat:

1.Koji model se dodaje
2. Uzmi formu u zavisnosti od tog modela, napravi slobodno 2 forme za uposlenika i za ucenika.
3. Redirectaj usera nazad na tabelu, za sad ga vrati na bilo koji model

'''

def dodaj_uposlenika(request):
    if request.method == "POST":
        form = UposlenikForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_uposlenika")
    else:
        form = UposlenikForm()
    return render(request, "radnici/dodaj_uposlenika.html", {"form": form})


'''
Ista logika kao za dodavanje.
Pitaj koji model se brise, uzmi id modela, izbrisi.

'''

def obrisi_uposlenika(request, pk):
    uposlenik = get_object_or_404(Uposlenik, pk=pk)
    uposlenik.delete()
    return redirect("lista_uposlenika")