from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Portafolio


class PortafolioView(ListView):
    model = Portafolio
    template_name = 'projects/portafolio.html'
    context_object_name = 'projects'


class PortafolioDetailView(ListView):
    model = Portafolio
    template_name = 'projects/portafoliodetail.html'
