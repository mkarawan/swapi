import itertools

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


@register.filter(name='sliced_dict')
def sliced_dict(dictionary):
    sliced_dictionary = dict(itertools.islice(dictionary.items(), 1, 5))
    return list(sliced_dictionary.items())


@register.filter(name='sliced_dict_films')
def sliced_dict_films(dictionary):
    sliced_dictionary = dict(itertools.islice(dictionary.items(), 2, 6))
    return list(sliced_dictionary.items())


register.filter("extract_id", extract_id)
register.filter("sliced_dict", sliced_dict)
register.filter("sliced_dict", sliced_dict_films)
