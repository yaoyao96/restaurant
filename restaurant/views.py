from django.shortcuts import get_object_or_404,render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.template import loader
from django.views import generic
from django.urls import reverse

from .models import Restaurant, Comment, User, Like


class IndexView(generic.ListView):
    template_name = 'restaurant/index.html'
    context_object_name = 'restaurant_list'
    def get_queryset(self):
        return Restaurant.objects.order_by('r_name')

class DetailView(generic.DetailView):
    model = Restaurant
    template_name = 'restaurant/detail.html'

class CommentView(generic.DetailView):
    model = Restaurant
    template_name = 'restaurant/comment.html'

def SubmitComment(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    new_user = User(u_name='')
    new_user.u_name = request.POST['name']
    new_user.save()
    new_comment = Comment(c_restaurant = restaurant, c_user = new_user)
    new_comment.c_rate = request.POST['rate']
    new_comment.c_desc = request.POST['desc']
    new_comment.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
    return HttpResponseRedirect(reverse('restaurant:detail', args=(restaurant.id,)))

def LikeComment(request, restaurant_id, comment_id):
   comment = get_object_or_404(Comment, pk=comment_id)
   comment.c_like += 1
   comment.save()
#    restaurant=comment.c_restaurant
   return HttpResponseRedirect(reverse('restaurant:detail', args=(restaurant_id,)))
    