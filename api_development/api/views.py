from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import requests


def listofcountries(request):
    r = requests.get('https://api.worldbank.org/v2/countries?format=json', params=request.GET)
    if r.status_code == 200:
        data = r.json()
        res = []
        for each in data[1]:
            dct = {}
            dct['name'] = each['name']
            dct['iso2Code'] = each['iso2Code']
            res.append(dct)
        return HttpResponse(res)
    return HttpResponse('Could not save data')

def populationyear(request, countryCode):
    r = requests.get('https://api.worldbank.org/v2/country/' + countryCode + '/indicator/SP.POP.TOTL?format=json', params=request.GET)
    if r.status_code == 200:
        data = r.json()
        country = ''
        res = []
        for each in data[1]:
            dct = {}
            dct['year'] = each['date']
            dct['population'] = each['value']
            country = each['country']['value']
            res.append(dct)
        res.insert(0,{'country': country})
        return HttpResponse(res)
    return HttpResponse("Could not fetched data")

def tempconvert(request, temperature):
    farenheit = (float(temperature) * 1.8)+32
    return HttpResponse([{'farenheit': str(farenheit)}])

