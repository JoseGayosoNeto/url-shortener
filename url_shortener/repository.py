from django.core.exceptions import ValidationError
from django.forms import ModelForm
from url_shortener.models import url_shortener


def get_all_urls():
    return url_shortener.objects.all()

def get_url_by_short_url(shorten_url):
    return url_shortener.objects.filter(shorten_url__exact=shorten_url).first()

def save_url_data(form_data: ModelForm):
    new_form_data = form_data
    
    if new_form_data.is_valid():
        new_form_data.save()
        return new_form_data
    
    return None
    
def update_in_1_url_visits(url_data: url_shortener):
    url_data.visits += 1
    url_data.save()