from typing import List

from django.db.models import Q
from django.http import HttpRequest
from django.shortcuts import render
from django.views import generic

from .forms import ItemForm
from .models import Item


def index(request: HttpRequest):
    query = request.GET.get("q")
    items = []
    if query:
        items: List[Item] = Item.objects \
            .filter(public=True) \
            .filter(Q(title__icontains=query) | Q(author__icontains=query))
    return render(request, "archive/index.html", {"items": items})


class IndexView(generic.FormView):
    template_name = "archive/index.html"
    form_class = ItemForm

    # context_object_name = 'latest_items'
    #
    # def get_queryset(self):
    #     return Item.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Item
    template_name = "archive/detail.html"


class ResultsView(generic.DetailView):
    model = Item
    template_name = "archive/results.html"
