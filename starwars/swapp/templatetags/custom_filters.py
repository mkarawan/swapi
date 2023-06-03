import itertools
import requests as requests
from django import template
import re

register = template.Library()


# custom filter to extract id from SWAPI url
@register.filter(name='extract_id')
def extract_id(url):
    pattern = r"/(\d+)/$"
    url_number = re.search(pattern, url)
    if url_number:
        return int(url_number.group(1))
    else:
        return None


# custom filter to slice dict data for category.html (more info)
@register.filter(name='sliced_dict')
def sliced_dict(dictionary):
    sliced_dictionary = dict(itertools.islice(dictionary.items(), 1, 5))
    return list(sliced_dictionary.items())


# custom filter to slice dict data for category.html (more info) - films category
@register.filter(name='sliced_dict_films')
def sliced_dict_films(dictionary):
    sliced_dictionary = dict(itertools.islice(dictionary.items(), 2, 6))
    return list(sliced_dictionary.items())


# custom filter to display proper values in details.html (from urls to names)
@register.filter(name='list_unpack')
def list_unpack(url_list):
    if isinstance(url_list, list):
        values_list = []
        for url in url_list:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                values = list(data.values())
                values_list.append(values[0])
        return ', '.join(values_list)

    elif isinstance(url_list, str) and url_list.startswith('https'):
        response = requests.get(url_list)
        if response.status_code == 200:
            data = response.json()
            values = list(data.values())
            return values[0]
    else:
        return url_list


# custom filter to replace "_" with " " for API results keys
@register.filter(name="underscore")
def underscore(string):
    return string.replace("_", " ")


# custom filter to extract date and time from 'created' and 'edited' values
@register.filter(name='format_date')
def format_date(string):
    if isinstance(string, str) and string.startswith('20'):
        formatted_date = string[:10] + " " + string[11:16]
        return formatted_date
    else:
        return string


# custom filter to cut first two sentences from opening crawl in api/films
@register.filter(name='cut')
def cut(string):
    if isinstance(string, str) and len(string) > 100:
        sentence_list = string.split('.')
        result = '. '.join(sentence_list[:2])
        return result + "..."
    else:
        return string


# custom filter to extract name or title for details.html
@register.filter(name='details')
def details(values):
    for i in values.keys():
        if i == "name" or "title":
            return values[i]
