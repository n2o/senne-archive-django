from django.views import generic

from .forms import ItemForm
from .models import Item


class IndexView(generic.FormView):
    template_name = 'archive/index.html'
    form_class = ItemForm
    succuess_url = '/'

    # context_object_name = 'latest_items'
    #
    # def get_queryset(self):
    #     return Item.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Item
    template_name = 'archive/detail.html'


class ResultsView(generic.DetailView):
    model = Item
    template_name = 'archive/results.html'
