# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
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


def bootstrap_elements(request):
    host_data = ""
    host_list = host_info.objects.all()

    latest_question_list = host_info.objects.order_by('id')

    context = {
        'latest_question_list': latest_question_list,
    }

    return render(request, 'opsc/bootstrap-elements.html', context)

def bootstrap_grid(request):
    host_data = ""
    host_list = host_info.objects.all()

    latest_question_list = host_info.objects.order_by('id')

    context = {
        'latest_question_list': latest_question_list,
    }

    return render(request, 'opsc/bootstrap-grid.html', context)

def forms(request):
    host_data = ""
    host_list = host_info.objects.all()

    latest_question_list = host_info.objects.order_by('id')

    context = {
        'latest_question_list': latest_question_list,
    }

    return render(request, 'opsc/forms.html', context)

def tables(request):
    host_data = ""
    host_list = host_info.objects.all()

    latest_question_list = host_info.objects.order_by('id')

    context = {
        'latest_question_list': latest_question_list,
    }

    return render(request, 'opsc/tables.html', context)


def table2(request):
    host_data = ""
    host_list = host_info.objects.all()

    latest_question_list = host_info.objects.order_by('id')

    context = {
        'latest_question_list': latest_question_list,
    }

    return render(request, 'opsc/table2.html', context)





def query_host(request, query_str):
    host_detail = get_object_or_404(host_info, id=query_str)
    context = {
        'host_detail': host_detail,
    }

    return render(request, 'opsc/host_detail.html.bak', context)


def add_host(request, str_id):
    return HttpResponse("Hello,  add_host %s." % str_id)


# Create your views here.
