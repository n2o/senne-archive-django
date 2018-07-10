from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404

from .models import Item, Author


def index(request: HttpRequest):
    query = request.GET.get("q")
    author_get = request.GET.get("autor")
    page = request.GET.get("page", 1)
    authors = Author.objects.all()
    author = __get_author_from_get_parameter(author_get)
    items_from_db = __query_items(query, author)
    prepared_items = __paginate_results(items_from_db, page)
    return render(request, "archive/index.html", {"items": prepared_items,
                                                  "forloop_modifier": 20 * (int(page) - 1),
                                                  "authors": authors})


def __get_author_from_get_parameter(author):
    try:
        if author:
            author = Author.objects.get(pk=int(author))
    except ValueError:
        author = None
    except ObjectDoesNotExist:
        author = None
    return author


def __paginate_results(items, page):
    paginator = Paginator(items, 20)
    try:
        prepared_items = paginator.page(page)
    except PageNotAnInteger:
        prepared_items = paginator.page(1)
    except EmptyPage:
        prepared_items = paginator.page(paginator.num_pages)
    return prepared_items


def __query_items(query: str, author: Author):
    if query:
        items = Item.objects \
            .filter(public=True) \
            .filter(Q(title__icontains=query) |
                    Q(abstract__icontains=query))
        return items.filter(author=author) if author else items
    return []


def detail(request: HttpRequest, pk: Item):
    item_db = get_object_or_404(Item, pk=pk)
    item = item_db if item_db.public else None
    return render(request, "archive/detail.html", {"item": item})
