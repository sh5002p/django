from django.urls import path
from . import views, niveau_views

urlpatterns = [
    #page pour les équipes
    path("ajout/", views.ajout),
    path("traitement/", views.traitement),
    path("",views.index),
    path("affiche/<int:id>/",views.affiche),
    path("update/<int:id>/", views.update),
    path("updatetraitement/<int:id>/f", views.updatetraitement),
    path("delete/<int:id>/", views.delete),
    #page pour leur niveau de jeu
    path('',niveau_views.indexniveau),
    path('ajoutniveau/', niveau_views.ajoutniveau),
    path("traitementniveau/",niveau_views.traitementniveau),
    path("afficheniveau/<int:id>/",niveau_views.afficheniveau),
    path("deleteniveau/<int:id>/", niveau_views.deleteniveau),
    path("updateniveau/<int:id>/",niveau_views.updateniveau),
    path("traitementupdateniveau/<int:id>/",niveau_views.updatetraitementniveau),
]