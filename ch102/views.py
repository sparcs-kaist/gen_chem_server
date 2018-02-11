# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from ch102.models import *
from django.core import serializers
from datetime import datetime
from django.utils import timezone


# Create your views here.
def CORSAllowResponse(response):
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    response["Access-Control-Max-Age"] = "3600"
    response["Access-Control-Allow-Headers"] = "*"
    return response

def notice(request):
    notice = Notice.objects.all().order_by('-post_date')
    notice = serializers.serialize('json', notice)
    response = JsonResponse(notice, safe=False)
    return CORSAllowResponse(response)

def schedule(request):
    schedule = Schedule.objects.all().order_by('event_date')
    schedule = serializers.serialize('json', schedule)
    return JsonResponse(schedule, safe=False)

def evaluation(request):
    evaluation = Evaluation.objects.all()
    evaluation = serializers.serialize('json', evaluation)
    return JsonResponse(evaluation, safe=False)

def links(request):
    links = Links.objects.all()
    links = serializers.serialize('json', links)
    response = JsonResponse(links, safe=False)
    return CORSAllowResponse(response)

def safety(request):
    safety = Safety.objects.all()
    safety = serializers.serialize('json', safety)
    return JsonResponse(safety, safe=False)

def contact(request):
    contact = Contact.objects.all().order_by('name')
    contact = serializers.serialize('json', contact)
    response = JsonResponse(contact, safe=False)
    return CORSAllowResponse(response)
