from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Uposlenik, Ucenik
from .forms import UposlenikForm


def lista_objekata(request, tip):
    if tip == "uposlenici":
        model = Uposlenik
        delete_url = "obrisi_uposlenika"
    elif tip == "ucenici":
        model = Ucenik
        delete_url = None   # za sad nemamo obrisi_ucenika
    else:
        return render(request, "404.html")



    queryset = model.objects.all().order_by("id")
    paginator = Paginator(queryset, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    
    varijable = [field.name for field in model._meta.get_fields()]

    vrijednosti = []
    for obj in page_obj:
        vrijednosti.append([getattr(obj, field) for field in varijable if field != "id"])

    return render(request, "UposleniciSkole/lista_uposlenika.html", {
        "tip": tip,
        "varijable": [field for field in varijable if field != "id"], 
        "vrijednosti": vrijednosti,
        "page_obj": page_obj,
        "delete_url": delete_url,
    })



def dodaj_uposlenika(request):
    if request.method == "POST":
        form = UposlenikForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_uposlenika")
    else:
        form = UposlenikForm()
    return render(request, "UposleniciSkole/dodaj_uposlenika.html", {"form": form})



def obrisi_uposlenika(request, pk):
    uposlenik = get_object_or_404(Uposlenik, pk=pk)
    uposlenik.delete()
    return redirect("lista_uposlenika")