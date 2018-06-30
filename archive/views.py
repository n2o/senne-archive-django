from django.db.models import Q
from django.http import HttpRequest, Http404
from django.shortcuts import render, get_object_or_404
from typing import List

from .models import Item


def index(request: HttpRequest):
    query = request.GET.get("q")
    items = []
    if query:
        items: List[Item] = Item.objects \
            .filter(public=True) \
            .filter(Q(title__icontains=query)) \
            .filter(Q(abstract__icontains=query))
    return render(request, "archive/index.html", {"items": items})


def detail(request: HttpRequest, pk: Item):
    item_db = get_object_or_404(Item, pk=pk)
    item = item_db if item_db.public else None
    if not item:
        raise Http404("Archiveintrag konnte nicht gefunden werden")
    return render(request, "archive/detail.html", {"item": item})
