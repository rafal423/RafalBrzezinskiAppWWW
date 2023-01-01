import datetime

from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone

class Druzyna(models.Model):
    nazwa = models.CharField(max_length=50)
    kraj = models.CharField(max_length=2,validators=[RegexValidator('^[A-Z]*$',
                               'Tylko duże litery.')],)
    def __str__(self):
        return '%s (%s)' % (self.nazwa, self.kraj)

    class Meta:
        ordering = ["nazwa"]
        verbose_name_plural = "drużyny"

class Osoba(models.Model):
    imie = models.CharField(max_length=50, blank=False)
    nazwisko = models.CharField(max_length=100, blank=False)
    class Miesiace (models.IntegerChoices):
        STYCZEN = 1, ("Styczeń")
        LUTY = 2, ("Luty")
        MARZEC = 3, ("Marzec")
        KWIECIEN = 4, ("Kwiecień")
        MAJ = 5, ("Maj")
        CZERWIEC = 6, ("Czerwiec")
        LIPIEC = 7, ("Lipiec")
        SIERPIEN = 8, ("Sierpień")
        WRZESIEN = 9, ("Wrzesień")
        PAZDZIERNIK = 10, ("Październik")
        LISTOPAD = 11, ("Listopad")
        GRUDZIEN = 12, ("Grudzień")
    miesiac_urodzenia = models.IntegerField(choices=Miesiace.choices, default=timezone.now().month)
    druzyna = models.ForeignKey(Druzyna, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return '%s %s' % (self.imie, self.nazwisko)

    class Meta:
        ordering = ["nazwisko"]
        verbose_name_plural = "osoby"

