from django.shortcuts import get_object_or_404,render

# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from django.template import loader

from .models import Restaurant


def index(request):
    restaurant_list = Restaurant.objects.order_by('-r_name')[:5]
    context = {
        'restaurant_list': restaurant_list,
    }
    return render(request, 'restaurant/index.html', context)

def detail(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    return render(request, 'restaurant/detail.html', {'restaurant':restaurant})