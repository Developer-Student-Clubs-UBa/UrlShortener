from django.db import models

from shortener.views import create_shortened_url


class ShortData(models.Model):
    made_on = models.DateTimeField(auto_now_add=True)
    long_url_format = models.URLField(verbose_name='Long Url')
    short_url_format = models.CharField(max_length=15, verbose_name='Short Url', unique=True, blank=False)

    class Meta:
        ordering = ['made_on']

    def __str__(self):
        return f'conversion of {self.long_url_format} to {self.short_url_format}'

    def save(self, *args, **kwargs):
        # If the short url wasn't specified
        if not self.short_url:
            # We pass the model instance that is being saved
            self.short_url = create_shortened_url(self)

        super().save(*args, **kwargs)