# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.

def notice(request):
    return JsonResponse({'notice': 'bar'})

def schedule(request):
    return JsonResponse({'schedule': 'bar'})

def evaluation(request):
    return JsonResponse({'evaluation': 'bar'})

def links(request):
    return JsonResponse({'links': 'bar'})

def safety(request):
    return JsonResponse({'safety': 'bar'})

def contact(request):
    return JsonResponse({'contact': 'bar'})