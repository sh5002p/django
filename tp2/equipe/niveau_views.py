from django.shortcuts import render, HttpResponseRedirect
from .forms import EquipeForm
from . import models


# Create your views here.


def ajoutniveau(request):
    if request.method == "POST":
        form = EquipeForm(request)
        return render(request,"tournois/niveau/ajout.html",{"form" : form})
    else :
        form = EquipeForm()
        return render(request,"tournois/niveau/ajout.html",{"form" : form})

def traitementniveau(request):
    lform = EquipeForm(request.POST)
    if lform.is_valid():
        equipe = lform.save()
        return HttpResponseRedirect("/tournois/niveau/")
    else :
        return render(request, "tournois/niveau/ajout.html", {"form": lform})
def indexniveau(request):
    liste = list(models.Equipe.objects.all())
    return render(request,"tournois/niveau/index.html",{"liste" : liste})

def afficheniveau(request, id):
    equipe = models.Equipe.objects.get(pk = id)
    return render(request, "tournois/niveau/affiche.html",{"tournois" : equipe})

def updateniveau(request, id):
    equipe = models.Equipe.objects.get(pk = id)
    form  = EquipeForm(equipe.dico())
    return render(request, "tournois/niveau/ajout.html", {"form" : form, "id" : id})

def updatetraitementniveau(request, id):
    lform = EquipeForm(request.POST)
    if lform.is_valid():
        equipe = lform.save(commit = False)
        equipe.id = id
        equipe.save()
        return HttpResponseRedirect("/tournois/niveau/")
    else:
        return render(request, "tournois/niveau/ajout.html", {"form": lform, "id" : id})

def deleteniveau(request, id):
    equipe = models.Equipe.objects.get(pk = id)
    equipe.delete()
    return HttpResponseRedirect("/tournois/niveau/")