from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404
from typing import List

from .models import Item


def index(request: HttpRequest):
    query = request.GET.get("q")
    page = request.GET.get("page", 1)
    items = []
    if query:
        items_db: List[Item] = Item.objects \
            .filter(public=True) \
            .filter(Q(title__icontains=query) |
                    Q(abstract__icontains=query))
        paginator = Paginator(items_db, 20)
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)
    return render(request, "archive/index.html", {"items": items, "forloop_modifier": 20 * (int(page) - 1)})


def detail(request: HttpRequest, pk: Item):
    item_db = get_object_or_404(Item, pk=pk)
    item = item_db if item_db.public else None
    return render(request, "archive/detail.html", {"item": item})
