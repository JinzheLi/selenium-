from django.core.paginator import Paginator
from django.shortcuts import render
from datetime import datetime
from common.models import Speeddate
from django.db.models import Q


def index(request):
    list = Speeddate.objects.all()
    context = {'inter': list}
    return render(request, "myadmin/type/index.html", context)
