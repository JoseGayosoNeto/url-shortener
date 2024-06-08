from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import url_shortener
from .service import create_short_link


@receiver(pre_save, sender=url_shortener)
def url_shortener_pre_save(sender, instance, **kwargs):
    if not instance.shorten_url:
        instance.shorten_url = create_short_link()