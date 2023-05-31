import re
from urllib.parse import urljoin

import requests as requests
from django.shortcuts import render, redirect
import json
from django.http import HttpResponseServerError
from django.views.decorators.cache import cache_page


@cache_page(60 * 15)
def get_swapi(request):
    url = 'https://swapi.dev/api/'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        results = list(data.keys())
        context = {'categories': results,
                   }
        return render(request, 'swapp/index.html', context)
    else:
        return HttpResponseServerError("Błąd podczas pobierania danych z API SWAPI")

@cache_page(60 * 15)
def get_swapi_category(request, cat_name):
    url = f'https://swapi.dev/api/{cat_name}/'
    page = request.GET.get('page')
    if page:
        url = page
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        category_results = data['results']
        next_page = data.get('next')
        previous = data.get('previous')
        context = {'category': category_results, 'cat_name': cat_name, 'next': next_page, 'previous': previous}
        return render(request, 'swapp/category.html', context)
    else:
        return HttpResponseServerError("Błąd podczas pobierania danych z API SWAPI")
@cache_page(60 * 15)
def get_swapi_details(request, cat_name, url_number):
    url = f'https://swapi.dev/api/{cat_name}/{url_number}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        context = {'results': [(key, value) for key, value in data.items()], 'cat_name': cat_name, 'url_number': url_number}
        return render(request, 'swapp/details.html', context)
    else:
        return HttpResponseServerError("Błąd podczas pobierania danych z API SWAPI")