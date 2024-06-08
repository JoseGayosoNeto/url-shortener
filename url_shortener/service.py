from django.core.exceptions import ValidationError
from django.http import HttpRequest
import random
import string
from .forms import NewUrlModelForm
from .models import url_shortener
from .repository import (
    get_all_urls, 
    save_url_data, 
    get_url_by_short_url, 
    update_in_1_url_visits,
)

def get_urls(request):
    urls = get_all_urls()
    
    query_params = request.GET.get('visits')
    if query_params:
        urls = urls.order_by('visits')
    
    return urls

def get_url_by_shorten_url(shorten_url):
    url = get_url_by_short_url(shorten_url)
    
    return url

def create_new_url_link(request: HttpRequest, shorten_url: str):
    return request.build_absolute_uri('/') + 'v1/' + shorten_url
    
def create_short_link():
    characters = string.ascii_letters + string.digits
    shorten_url = ''.join(random.choices(characters, k=5))
    
    while get_url_by_short_url(shorten_url):
        shorten_url = ''.join(random.choices(characters, k=5))
    
    return shorten_url

def save_form_data(form: NewUrlModelForm):
    saved_data = save_url_data(form)
    if type(saved_data) != ValidationError:
        return saved_data
    
    return saved_data.message

def update_url_visits(url: url_shortener):
    update_in_1_url_visits(url)
    