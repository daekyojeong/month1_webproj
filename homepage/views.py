from . import data_init
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import OTT

# Create your views here.
def index(request):
    ott_data = OTT.objects.all()
    if not ott_data:
        i = data_init.init()
    else:
        i = len(ott_data)

    init(ott_data)

    data = {"all": len(ott_data), "netflix":0, "hulu":0, "pv":0, "disney":0}
    selected = ['all']
    for item in ott_data:
        data["netflix"] += item.netflix
        data["hulu"] += item.hulu
        data["pv"] += item.primevideo
        data["disney"] += item.disneyplus

    if request.method == "POST":
        selected = request.POST.getlist('genre')
        genres_data = genres_q(selected, ott_data)
        return render(request, 'index.html', {"data":genres_data, "selected":selected})


    return render(request, 'index.html', {"data":data, "selected":selected})

def init(ott_data):
    year_range = []



def genres_q(selected, ott_data):
    genres_data = {"all": len(ott_data), "netflix":0, "hulu":0, "pv":0, "disney":0}
    cnt=0
    for item in ott_data:
        g = str(item.genres)
        g.split(',')
        if 'all' in selected:
            genres_data["netflix"] += item.netflix
            genres_data["hulu"] += item.hulu
            genres_data["pv"] += item.primevideo
            genres_data["disney"] += item.disneyplus
            cnt += 1
        else:
            for select in selected:
                if select in g:
                    genres_data["netflix"] += item.netflix
                    genres_data["hulu"] += item.hulu
                    genres_data["pv"] += item.primevideo
                    genres_data["disney"] += item.disneyplus
                    cnt += 1
                    break
    genres_data["all"] = cnt
    return genres_data
