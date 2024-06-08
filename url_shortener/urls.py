from django.urls import path
from .views import URLShortenerListView, NewURLShortenedView, URLRedirectView


urlpatterns = [
    path('urls/', URLShortenerListView.as_view(), name='urls-list'),
    path('', NewURLShortenedView.as_view(), name='shorten-url'),
    path('<str:shorten_url>/', URLRedirectView.as_view(), name='url-redirect')
]
