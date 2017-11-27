# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from .models import TYPE_RC


# Create your views here.
def index(request):
  return render(request, 'index.html')

def detail(request, type_id):
  type_id = int(type_id)
  context = {'type_id': type_id, 'type': TYPE_RC[type_id-1], 'types': TYPE_RC}
  return render(request, 'type_text_input.html', context)

def calculate(request):
  print(request.POST)
  # type = request.GET.type
  # value = request.GET.value
  # print(type, value)
  return HttpResponse.is_ajax('success')