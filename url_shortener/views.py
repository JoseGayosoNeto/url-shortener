from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views import View
from .forms import NewUrlModelForm
from .service import (
    get_urls,
    save_form_data,
    get_url_by_shorten_url,
    update_url_visits,
    create_new_url_link,
)


class URLShortenerListView(View):
    
    def get(self, request):
        urls = get_urls(request)
        if not urls:
            messages.info(request, 'No shortered urls found.')
        
        return render(request, 'stats.html', {'urls': urls})
    
class NewURLShortenedView(View):
    def get(self, request):
        
        new_url_form = NewUrlModelForm()
        
        return render(request, 'shorten_url.html', {'new_url_form': new_url_form})
    
    def post(self, request:HttpRequest):
        
        new_url_form_data = NewUrlModelForm(request.POST)
        if not new_url_form_data:
            return redirect('shorten-url')
        
        url_data = save_form_data(new_url_form_data)
        if url_data:
            new_url_link = create_new_url_link(request, url_data.instance.shorten_url)
        
            context = {
                'new_url_form': new_url_form_data,
                'new_url_link': new_url_link
            }
            
            return render(request, 'shorten_url.html', context=context)
        
        context = {
            'new_url_form': new_url_form_data
        }
        
        return render(request, 'shorten_url.html', context=context)

class URLRedirectView(View):
    
    def get(self, request: HttpRequest, shorten_url: str):
        url = get_url_by_shorten_url(shorten_url)
        if not url:
            messages.warning(request, "URL doesn't exist")
            return redirect('shorten-url')
        
        update_url_visits(url)
        
        return redirect(url.original_url)
