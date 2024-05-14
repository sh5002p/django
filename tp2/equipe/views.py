from django.shortcuts import render, HttpResponseRedirect
from .forms import EquipeForm
from . import models


# Create your views here.


def ajout(request):
    if request.method == "POST":
        form = EquipeForm(request)
        return render(request,"tournois/equipe/ajout.html",{"form" : form})
    else :
        form = EquipeForm()
        return render(request,"tournois/equipe/ajout.html",{"form" : form})

def traitement(request):
    lform = EquipeForm(request.POST)
    if lform.is_valid():
        equipe = lform.save()
        return HttpResponseRedirect("/tournois/equipe/")
    else :
        return render(request, "tournois/equipe/ajout.html", {"form": lform})
def index(request):
    liste = list(models.Equipe.objects.all())
    return render(request,"tournois/equipe/index.html",{"liste" : liste})

def affiche(request, id):
    equipe = models.Equipe.objects.get(pk = id)
    return render(request, "tournois/equipe/affiche.html",{"tournois" : equipe})

def update(request, id):
    equipe = models.Equipe.objects.get(pk = id)
    form  = EquipeForm(equipe.dico())
    return render(request, "tournois/equipe/ajout.html", {"form" : form, "id" : id})

def updatetraitement(request, id):
    lform = EquipeForm(request.POST)
    if lform.is_valid():
        equipe = lform.save(commit = False)
        equipe.id = id
        equipe.save()
        return HttpResponseRedirect("/tournois/equipe/")
    else:
        return render(request, "tournois/equipe/ajout.html", {"form": lform, "id" : id})

def delete(request, id):
    equipe = models.Equipe.objects.get(pk = id)
    equipe.delete()
    return HttpResponseRedirect("/tournois/equipe/")