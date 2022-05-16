from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models


class carMarqueForm(ModelForm):
    class Meta:
        model = models.car_marque
        fields = ("marque",)
        labels = {
            "marque": _("Marque de la voiture"),
        }


class carForm(ModelForm):
    class Meta:
        model = models.car
        fields = ("name", "horses", "release_date", "marque")
        labels = {
            "name": _("Modèle"),
            "horses": _("Nombre de cheveaux"),
            "release_date": _("Année de sortie"),
            "marque": _("Marque de la voiture"),
        }


class motorcycleForm(ModelForm):
    class Meta:
        model = models.motorcycle
        fields = ("name", "cylinder", "release_date")
        labels = {
            "name": _("Modèle"),
            "cylinder": _("Cylindrée"),
            "release_date": _("Année de sortie"),
        }
