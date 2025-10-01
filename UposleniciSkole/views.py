from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Uposlenik, Ucenik
from .forms import UposlenikForm
from .forms import UcenikForm    # Ovdje sam stavio ovu liniju, promjeni ako zapne kod


def lista_objekata(request, model_name):
    if model_name == "uposlenici":
        model = Uposlenik
        delete_url = "obrisi_uposlenika"
        template = "radnici/lista_uposlenika.html"
    elif model_name == "ucenici":
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


    return render(request,"radnici/lista_objekata.html", {
        "model_name": model_name,
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
            return redirect("lista_objekata", model_name="uposlenici")
    else:
        form = UposlenikForm()
    return render(request, "radnici/lista_objekata.html", {"form": form})



def obrisi_uposlenika(request, pk):
    uposlenik = get_object_or_404(Uposlenik, pk=pk)
    uposlenik.delete()
    return redirect("lista_objekata", model_name="uposlenici")






def dodaj_ucenika(request):
    if request.method == "POST":
        form = UcenikForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_objekata", model_name="ucenici")
    else:
        form = UcenikForm()
    return render(request, "radnici/lista_objekata.html", {"form": form})






