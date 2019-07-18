from django.shortcuts import get_object_or_404,render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.template import loader
from django.views import generic
from django.urls import reverse
from django.db.models import Avg

from .models import Restaurant, Review, User, Comment


class IndexView(generic.ListView):
    template_name = 'restaurant/index.html'
    context_object_name = 'restaurant_list'
    def get_queryset(self):
        return Restaurant.objects.order_by('r_name')

def detail(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    review_number = restaurant.review_set.count()
    average_rate = restaurant.review_set.aggregate(Avg('r_rate'))
    context = {'restaurant': restaurant, 'review_number': review_number, 'average_rate': average_rate}
    return render(request, 'restaurant/detail.html', context)

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

def comment(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    context = {'review': review, 'user': review.r_user.u_name, 'description': review.r_desc}
    return render(request, 'restaurant/comment.html', context)

def SubmitComment(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    new_user = User(u_name='')
    new_user.u_name = request.POST['name']
    new_user.save()
    new_comment = Comment(c_review = review, c_user = new_user)
    new_comment.c_desc = request.POST['desc']
    new_comment.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
    return HttpResponseRedirect(reverse('restaurant:detail', args=(review.r_restaurant.id,)))

def reply(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    context = {'review': comment.c_review, 'user': comment.c_user.u_name, 'description': comment.c_desc, 'comment': True}
    return render(request, 'restaurant/comment.html', context)

def SubmitReply(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    new_user = User(u_name='')
    new_user.u_name = request.POST['name']
    new_user.save()
    new_comment = Comment(c_review = review, c_user = new_user)
    new_comment.c_desc = request.POST['desc']
    new_comment.c_reply_user = request.POST['reply_user']
    new_comment.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
    return HttpResponseRedirect(reverse('restaurant:detail', args=(review.r_restaurant.id,)))