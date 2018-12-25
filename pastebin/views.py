from django.shortcuts import render
from django.views.generic import CreateView,DetailView,ListView, DeleteView, UpdateView
from .models import Paste
from django.urls import reverse_lazy
# Create your views here.


class PasteView(CreateView):
    model = Paste
    fields = ['text', 'name']


class PasteDetail(DetailView):

    model = Paste
    template_name = 'pastebin/paste_detail.html'


class PasteList(ListView):

    queryset = Paste.objects.all()


class PasteUpdate(UpdateView):

    model = Paste
    fields = ['text', 'name']


class PasteDelete(DeleteView):

    model = Paste
    success_url = reverse_lazy('pastebin_paste_list')








