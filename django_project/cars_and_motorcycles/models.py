from django.db import models


class marque(models.Model):
    marque = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return f"{self.marque}"

    def dico(self):
        return {
            "marque": self.marque
        }


class car(models.Model):
    name = models.CharField(max_length=100, blank=False)
    designer = models.CharField(max_length=100, blank=False)
    horses = models.IntegerField(blank=False)
    release_date = models.IntegerField(blank=True)
    marque = models.ForeignKey(marque, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Modèle: {self.name} | Concepteur: {self.designer} | Cheveaux: {self.horses} | Année de sortie: {self.release_date} | Marque : {self.marque}"

    def dico(self):
        return {
            "name": self.name,
            "designer": self.designer,
            "horses": self.horses,
            "release_date": self.release_date,
            "marque": self.marque,
        }


class motorcycle(models.Model):
    name = models.CharField(max_length=100, blank=False)
    designer = models.CharField(max_length=100, blank=False)
    cylinder = models.IntegerField(blank=False)
    release_date = models.IntegerField(blank=True)

    def __str__(self):
        return f"Modèle: {self.name} | Concepteur: {self.designer} | Cylindrée: {self.cylinder} | Année de sortie: {self.release_date}"

    def dico(self):
        return {
            "name": self.name,
            "designer": self.designer,
            "cylinder": self.cylinder,
            "release_date": self.release_date,
        }