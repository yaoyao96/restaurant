from django.shortcuts import get_object_or_404,render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.template import loader
from django.views import generic
from django.urls import reverse

from .models import Restaurant, Review, User, Comment


class IndexView(generic.ListView):
    template_name = 'restaurant/index.html'
    context_object_name = 'restaurant_list'
    def get_queryset(self):
        return Restaurant.objects.order_by('r_name')

class DetailView(generic.DetailView):
    model = Restaurant
    template_name = 'restaurant/detail.html'

class ReviewView(generic.DetailView):
    model = Restaurant
    template_name = 'restaurant/review.html'

def SubmitReview(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    new_user = User(u_name='')
    new_user.u_name = request.POST['name']
    new_user.save()
    new_review = Review(r_restaurant = restaurant, r_user = new_user)
    new_review.r_rate = request.POST['rate']
    new_review.r_desc = request.POST['desc']
    new_review.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
    return HttpResponseRedirect(reverse('restaurant:detail', args=(restaurant.id,)))

def LikeReview(request, restaurant_id, review_id):
   review = get_object_or_404(Review, pk=review_id)
   review.r_like += 1
   review.save()
#    restaurant=review.r_restaurant
   return HttpResponseRedirect(reverse('restaurant:detail', args=(restaurant_id,)))
    