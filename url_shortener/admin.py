from django.contrib import admin
from .models import url_shortener


class UrlShortenerAdmin(admin.ModelAdmin):
    list_display = ('original_url', 'shorten_url', 'created_at', 'visits')
    search_fields = ('original_url', 'shorten_url', 'created_at', 'visits')
    
admin.site.register(url_shortener, UrlShortenerAdmin)
