from typing import Any
from django.db import models
import string
from random import choices


class url_shortener(models.Model):
    created_at = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    original_url = models.URLField(max_length=512, null=False, blank=False)
    shorten_url = models.CharField(max_length=5, null=False, blank=False, unique=True)
    visits = models.IntegerField(null=False, blank=False, default= 0)
    
    def __str__(self):
        return f"Original URL: '{self.original_url}' - Shorten_url: '{self.shorten_url}' - DateTime: '{self.created_at}'"