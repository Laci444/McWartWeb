from django.urls import path
from .views import *



urlpatterns = [
    path('', indexView, name='index'),
    path('wayback', waybackView, name='wayback'),
    path('idogep', timebackView, name='timemachine'),
    path('miertdebrecen', prView, name='pr'),
]
