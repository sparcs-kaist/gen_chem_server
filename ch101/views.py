from django.shortcuts import render
from django.http import JsonResponse
from ch101.models import *
from django.core import serializers
from datetime import datetime
from django.utils import timezone
from django.conf import settings

import ast

# Create your views here.
def CORSAllowResponse(response):
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    response["Access-Control-Max-Age"] = "3600"
    response["Access-Control-Allow-Headers"] = "*"
    return response

def CORSAllowResponse(response):
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    response["Access-Control-Max-Age"] = "3600"
    response["Access-Control-Allow-Headers"] = "*"
    return response

def notice(request):
    notice = Notice.objects.all().order_by('-post_date')
    notice = serializers.serialize('json', notice)
    return JsonResponse(notice, safe=False)

def schedule(request):
    schedule = Schedule.objects.all().order_by('event_date')
    schedule = serializers.serialize('json', schedule)
    return JsonResponse(schedule, safe=False)

def download(request):
    download = {}
    download ["media_url"] = settings.MEDIA_URL

    data = Download.objects.all().order_by('-year')
    data = serializers.serialize('json', data)
    download ["data"] = ast.literal_eval (data)

    response = JsonResponse(download, safe=False)
    return CORSAllowResponse (response)

def contact(request):
    contact = Contact.objects.all().order_by('name')
    contact = serializers.serialize('json', contact)
    return JsonResponse(contact, safe=False)
