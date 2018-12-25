from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Car
# Create your views here.


class CarListView(ListView):

    queryset = Car.objects.all()

#
# class CarDetailView(DetailView):
#
