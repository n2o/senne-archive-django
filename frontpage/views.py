from django.shortcuts import render

from frontpage.models import Frontpage


def index(request):
    frontpage = Frontpage.objects.first()
    return render(request, "frontpage/index.html", {"frontpage": frontpage})
