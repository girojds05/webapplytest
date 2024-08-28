from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Book
# Create your views here.

class ListBookView(ListView):
    model = Book
    template_name = 'book/book_list.html'

class DetailBoookView(DetailView):
    template_name = 'book/book_detail.html'
    model = Book

class CreateBookView(CreateView):
    model = Book
    template_name = 'book/book_create.html'
    fields = ('title', 'text', 'category')
    success_url = reverse_lazy('list-book')
    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super().form_valid(form)

class DeleteBookView(DeleteView):
    model = Book
    template_name = 'book/book_confirm_delete.html'
    success_url = reverse_lazy('list-book')

class UpdateBookView(UpdateView):
    model = Book
    template_name = 'book/book_update.html'
    fields = (['title', 'text', 'category'])
    success_url = reverse_lazy('list-book')