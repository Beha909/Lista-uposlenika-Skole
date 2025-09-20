from django.shortcuts import render, redirect, get_object_or_404
from .models import Uposlenik
from .forms import UposlenikForm
from django.core.paginator import Paginator




# Create your views here.


def lista_uposlenika(request):
    uposlenici = Uposlenik.objects.all().order_by("id")
    paginator = Paginator(uposlenici, 10)  
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "radnici/lista_uposlenika.html", {"page_obj": page_obj})      # Ako ne bude funkcionisalo, requesta stavi templates


def dodaj_uposlenika(request):
    if request.method == "POST":
        form = UposlenikForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_uposlenika")
    else:
        form = UposlenikForm()
    return render(request, "radnici/dodaj_uposlenika.html", {"form": form})

def obrisi_uposlenika(request, pk):
    uposlenik = get_object_or_404(Uposlenik, pk=pk)
    uposlenik.delete()
    return redirect("lista_uposlenika")