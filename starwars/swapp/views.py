import requests as requests
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
import json
from django.http import HttpResponseServerError




def get_swapi(request):
    url = 'https://swapi.dev/api/'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        results = list(data.keys())
        # url_list = []
        # for name in results:
        #     url_list.append(url + name)
        context = {'categories': results,
                   # 'url': url_list,
                   }
        return render(request, 'swapp/index.html', context)
    else:
        return HttpResponseServerError("Błąd podczas pobierania danych z API SWAPI")


def get_swapi_category(request, cat_name):
    url = f'https://swapi.dev/api/{cat_name}/'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        category_results = data['results']

        context = {'category': category_results, 'cat_name': cat_name}
        return render(request, 'swapp/category.html', context)
    else:
        return HttpResponseServerError("Błąd podczas pobierania danych z API SWAPI")

def get_swapi_details(request, id):
    pass