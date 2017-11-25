from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.

def notice(request):
    return JsonResponse({'notice': 'bar'})

def schedule(request):
    return JsonResponse({'schedule': 'bar'})

def download(request):
    return JsonResponse({'download': 'bar'})

def contact(request):
    return JsonResponse({'contact': 'bar'})