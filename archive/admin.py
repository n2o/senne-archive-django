from django.contrib import admin
from reversion.admin import VersionAdmin

from .models import Item


@admin.register(Item)
class ItemAdmin(VersionAdmin):
    list_display = ('title', 'author', 'medart', 'public', 'modified')
    list_filter = ['medart', 'source_datetime']
    search_fields = ['title', 'author']
    save_as = True
    readonly_fields = ['created', 'modified']
    ordering = ('-modified',)

    fieldsets = [
        ('Titel und Verfasser',
         {'fields': [
             'title', 'author', 'role'
         ]}),
        ('Quelle',
         {'fields': [
             'source_title', 'amount',
             'medart', 'location',
             ('year', 'source_datetime', 'number'),
             ('pages', 'place'),
             'notes', 'owner'
         ]}),
        ('Abstract',
         {'fields': [
             'abstract'
         ]}),
        ('Dateien',
         {'fields': [
             ('file1', 'file2', 'file3'),
             ('image1', 'image2', 'image3'),
         ]}),
        ('Meta-Informationen',
         {'fields': [
             'public',
             ('created', 'modified'),
         ]}),
    ]
