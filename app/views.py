# coding=utf8
# -*- coding: utf8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app.models import *

def landing(request):
	return render(request, 'index.min.html', {"title": "DARE, Dar Experiencias"})

def promos(request):
	return JsonResponse(dict(Promos=list(Promos.objects.values('title', 'short_desc', 'long_desc', 'location', 'contact', 'image_url', 'price'))))

def wishes(request):
	return JsonResponse(dict(Deseos=list(Wishes.objects.values('name', 'short_desc', 'cost', 'contact', 'video_url', 'approved'))))

@csrf_exempt
def makeawish(request):
	print request.method
	bulk_data = request.POST
	print bulk_data
	return HttpResponse(bulk_data)