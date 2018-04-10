# -*- coding: utf-8 -*-
from datetime import datetime

from django.db import models


class Item(models.Model):
    medart_choices = (
        ("Audiodatei", "Audiodatei"),
        ("Buch", "Buch"),
        ("CD / DVD", "CD / DVD"),
        ("Dia(s)", "Dia(s)"),
        ("Filmspule", "Filmspule"),
        ("Foto(s)", "Foto(s)"),
        ("Gegenstand", "Gegenstand"),
        ("Kassette", "Kassette"),
        ("Schallplatte", "Schallplatte"),
        ("Schrifttum", "Schrifttum"),
        ("Sonstiges", "Sonstiges"),
        ("Stempel", "Stempel"),
        ("Tonband", "Tonband"),
        ("VHS", "VHS"),
        ("Videodatei", "Videodatei"),
    )
    # Titel und Verfasser
    title = models.CharField("Titel *", max_length=1024, blank=False)
    author = models.CharField("Verfasser", max_length=256, blank=True)
    role = models.CharField("Rolle", max_length=256, blank=True)

    # Quelle
    medart = models.CharField("Medienart *", max_length=256, choices=medart_choices, blank=False)
    source_title = models.CharField("Quelltitel", max_length=1024, blank=True)
    abstract = models.TextField("Abstract", blank=True)
    year = models.IntegerField("Jahrgang", null=True, default=datetime.now().year, blank=True)
    number = models.CharField("Nummer", max_length=256, blank=True)
    source_datetime = models.DateTimeField("Datum", blank=True)
    pages = models.CharField("Seiten", max_length=256, blank=True)
    notes = models.TextField("Anmerkungen", blank=True)
    place = models.CharField("Ort / Veröffentlichung", max_length=256, blank=True)

    keywords = models.TextField("Schlagworte *", default="", blank=True, max_length=1024)
    location = models.CharField("Standort (analoges Archiv)", max_length=256, blank=True)
    amount = models.IntegerField("Anzahl / Exemplare", default=1, null=True, blank=True)
    owner = models.CharField("Besitzer", max_length=256, blank=True)
    public = models.BooleanField("Veröffentlichen?", default=False)

    file1 = models.FileField("1. Datei", upload_to="archive/", blank=True)
    file2 = models.FileField("2. Datei", upload_to="archive/", blank=True)
    file3 = models.FileField("3. Datei", upload_to="archive/", blank=True)

    image1 = models.ImageField("1. Abbildung", upload_to="archive/", blank=True)
    image2 = models.ImageField("2. Abbildung", upload_to="archive/", blank=True)
    image3 = models.ImageField("3. Abbildung", upload_to="archive/", blank=True)

    created = models.DateTimeField("Hinzugefügt am", default=datetime.now)
    modified = models.DateTimeField("Zuletzt geändert", auto_now=True)

    def __str__(self):
        return str(self.title)
