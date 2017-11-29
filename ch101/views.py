from django.shortcuts import render
from django.http import JsonResponse
from ch101.models import *
from django.core import serializers
from datetime import datetime
from django.utils import timezone


# Create your views here.

def notice(request):
    notice = Notice.objects.all().order_by('-event_date')
    notice = serializers.serialize('json', notice)
    print(notice)
    return JsonResponse(notice, safe=False)

def schedule(request):
    schedule = Schedule.objects.all().order_by('-event_date')
    schedule = serializers.serialize('json', schedule)
    return JsonResponse(schedule, safe=False)

def download(request):
    download = Download.objects.all().order_by('-date')
    download = serializers.serialize('json', download)
    return JsonResponse(download, safe=False)

def contact(request):
    contact = Contact.objects.all().order_by('name')
    contact = serializers.serialize('json', contact)
    return JsonResponse(contact, safe=False)
