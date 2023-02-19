from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/analytics/', about_analytics, name='analytics'),
    path('about/django/', about_django, name='django'),

]