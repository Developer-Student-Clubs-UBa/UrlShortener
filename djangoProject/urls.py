"""
A warm Welcome by the DSC core team, url shortener is the aim here. Fork it!
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shortener.urls')),
]
