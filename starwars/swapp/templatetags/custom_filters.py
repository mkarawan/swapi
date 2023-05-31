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


register.filter("extract_id", extract_id)
