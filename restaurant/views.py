from django.shortcuts import get_object_or_404,render

# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from django.views import generic

from .models import Restaurant


class IndexView(generic.ListView):
    template_name = 'restaurant/index.html'
    context_object_name = 'restaurant_list'
    def get_queryset(self):
        """Return the last five published questions."""
        return Restaurant.objects.order_by('r_name')

class DetailView(generic.DetailView):
    model = Restaurant
    template_name = 'restaurant/detail.html'