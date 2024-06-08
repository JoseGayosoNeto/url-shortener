from django import forms
import re
from .models import url_shortener


class NewUrlModelForm(forms.ModelForm):
    class Meta:
        model = url_shortener
        fields = ('original_url',)

    def clean_original_url(self):
        url_pattern = re.compile(
            r'^(https?|ftp):\/\/'  # protocol: either http, https, or ftp, followed by ://
            r'(?:(?:[a-zA-Z0-9$-_@.&+!*"(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'  # domain name: includes alphanumeric characters and some special characters, or percent-encoded characters
            r'(?:\.[a-zA-Z]{2,})+)'  # top-level domain: starts with a dot followed by at least two alphabetic characters
            r'(?::\d{2,5})?'  # optional port: a colon followed by 2 to 5 digits
            r'(?:\/[^\s]*)?$'  # optional path: starts with a slash followed by any non-whitespace characters
        )
        original_url = self.cleaned_data.get('original_url')
        if not url_pattern.match(original_url):
            self.add_error('original_url', 'This is not a valid URL.')
        
        return original_url

