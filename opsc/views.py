# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import host_info


def index(request):
    host_data = ""
    host_list = host_info.objects.all()

    latest_question_list = host_info.objects.order_by('id')

    context = {
        'latest_question_list': latest_question_list,
    }

    return render(request, 'opsc/index.html', context)


def add_host(request, str_id):
    return HttpResponse("Hello,  add_host %s." % str_id)

def query_host(request, query_str):
    host_detail = host_info.objects.get(id=query_str)
    context = {
        'host_detail': host_detail,
    }

    return render(request, 'opsc/host_detail.html', context)



# Create your views here.
