from django.shortcuts import render
from django.http import HttpResponse

def index (request):

    html = "" + '<a href = "/rango/about/"> Rango says hey there partner!</a>'

    return HttpResponse(html)

def about (request):

    html = "" + '<a href = "/rango/about/"> Rango says here is the about page. </a>'

    return HttpResponse(html)