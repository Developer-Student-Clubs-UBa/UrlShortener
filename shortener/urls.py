from django.urls import path

from shortener.views import *

urlpatterns = [
    path('', home, name='home'),  # Home page url (function based)
    path('', FirstView.as_view(), name='index'),  # Home page url (Class based)
]
