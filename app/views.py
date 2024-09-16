from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def odia (request):
    return HttpResponse('this is our odia movie function')

def preeti(request):
    return HttpResponse('My name is Preeti')