from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models


class MarqueForm(ModelForm):
    class Meta:
        pass


class carForm(ModelForm):
    class Meta:
        model = models.car
        fields = ("name", "designer", "horses", "release_date", "marque")
        labels = {
            "name": _("Modèle"),
            "designer": _("Concepteur"),
            "horses": _("Nombre de cheveaux"),
            "release_date": _("Année de sortie"),
            "marque": _("Marque de la voiture")
        }


class motorcycleForm(ModelForm):
    class Meta:
        model = models.motorcycle
        fields = ("name", "designer", "cylinder", "release_date")
        labels = {
            "name": _("Modèle"),
            "designer": _("Concepteur"),
            "cylinder": _("Cylindrée"),
            "release_date": _("Année de sortie"),
        }
