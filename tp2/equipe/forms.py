from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class EquipeForm(ModelForm):
    class Meta:
        model = models.Equipe
        fields = {'nom', 'nbr_joueurs', 'ville_assignee', 'date_creation', 'niveau'}
        labels = {
            'nom' : _('Nom'),
            'nbr_joueurs' : _('Nbr_joueurs'),
            'ville_assignee' : _('Ville Assignee'),
            'date_creation' : _('Date'),
            'niveau' : _('Niveau')
        }

class NiveauForm(ModelForm):
    class Meta:
        model = models.Niveau
        fields = ('avis', 'particularite')
        labels = {
            'avis' : _('Mon avis de leur niveau'),
        }