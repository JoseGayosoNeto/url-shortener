# Generated by Django 5.0.6 on 2024-05-29 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener', '0002_alter_url_shortener_shorten_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url_shortener',
            name='original_url',
            field=models.URLField(max_length=512),
        ),
    ]
