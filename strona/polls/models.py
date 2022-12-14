import datetime

from django.db import models
from django.utils import timezone

class Osoba(models.Model):
    imie = models.CharField(max_length=50, blank=False)
    nazwisko = models.CharField(max_length=100, blank=False)
    STYCZEN =  'ST'
    LUTY =  'LU'
    MARZEC =  'MA'
    KWIECIEN =  'KW'
    MAJ =  'MJ'
    CZERWIEC =  'CZ'
    LIPIEC =  'LI'
    SIERPIEN =  'SI'
    WRZESIEN =  'WR'
    PAZDZIERNIK =  'PA'
    LISTOPAD =  'LS'
    GRUDZIEN =  'GR'
    miesiace_wybory = [
        (STYCZEN, 'Styczeń'),
        (LUTY, 'Luty'),
        (MARZEC, 'Marzec'),
        (KWIECIEN, 'Kwiecień'),
        (MAJ, 'Maj'),
        (CZERWIEC, 'Czerwiec'),
        (LIPIEC, 'Lipiec'),
        (SIERPIEN, 'Sierpień'),
        (WRZESIEN, 'Wrzesień'),
        (PAZDZIERNIK, 'Październik'),
        (LISTOPAD, 'Listopad'),
        (GRUDZIEN, 'Grudzień'),
    ]
    miesiac_urodzenia = models.CharField(
        max_length=2,
        choices=miesiace_wybory,
        default=STYCZEN,
    )