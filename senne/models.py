from datetime import datetime

from django.db import models


class CreatedModifiedModel(models.Model):
    created = models.DateTimeField("Hinzugefügt am", default=datetime.now)
    modified = models.DateTimeField("Zuletzt geändert", auto_now=True)

    class Meta:
        abstract = True
