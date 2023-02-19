from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .utils import *
from .models import *
from .forms import *


class BooksList(DataMixin, ListView):   # 'ListView' create 'object_list'
    paginate_by = 5   # count of elements on the page
    model = Books
    template_name = 'books/books.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Книги')
        return dict(list(context.items()) + list(c_def.items()))   # combine (объединяем) classes ‘context’ & c_def (local data for transferring)


class ShowBook(DataMixin, DetailView):
    model = Books
    template_name = 'books/book.html'
    context_object_name = 'book'

    def get_context_data(self, *, object_list=None, **kwargs):  # for transfer dynamic data
        context = super().get_context_data(**kwargs)  # mandatory (обязательное) condition
        c_def = self.get_user_context(title= context['book'])
        return dict(list(context.items()) + list(c_def.items()))   # combine (объединяем) classes ‘context’ & c_def (local data for transferring)

class AddBook(LoginRequiredMixin, DataMixin, CreateView):  # 'LoginRequiredMixin' on first place!!!
   # 'LoginRequiredMixin' make this class only for authorized users
   form_class = AddBookForm
   template_name = 'books/addbook.html'
   login_url = reverse_lazy('admin:index')  # redirecting for unauthorized users to authorization page
   # show mistake 403 for unauthorized users: 'raise_exception = True
   def get_context_data(self, *, object_list=None, **kwargs):
       context = super().get_context_data(**kwargs)
       c_def = self.get_user_context(title= 'Add a book')
       return dict(list(context.items()) + list(c_def.items()))   # combine (объединяем) classes ‘context’ & c_def (local data for transferring)


