from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', BooksList.as_view(), name='books'),
    path('add/', AddBook.as_view(), name='addbook'),
    path('book/<slug:slug>/', ShowBook.as_view(), name='book'),
]