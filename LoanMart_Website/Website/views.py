from __future__ import unicode_literals
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def terms_and_condition_page(request):
    return render(request, 'terms_and_condition.html')
