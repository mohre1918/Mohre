# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render


def get_input(request):
    mgw = request.POST.getlist('MGW')

    source_operator = request.POST.getlist('source_operator')
    destination_operator = request.POST.getlist('destination_operator')
    start_date = request.POST.getlist('start_date')
    end_date = request.POST.getlist('end_date')
    a = ['   ']
    return "salam"
