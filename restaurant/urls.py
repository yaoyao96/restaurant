from django.urls import path

from . import views

app_name = 'restaurant'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # ex: /restaurant/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /restaurant/5/review
    path('<int:pk>/review/', views.ReviewView.as_view(), name='review'),
    # ex: /restaurant/5/submitreview
    path('<int:restaurant_id>/submitreview/', views.SubmitReview, name='SubmitReview'),
    # ex: /restaurant/5/likereview
    path('<int:restaurant_id>/<int:review_id>/likereview/', views.LikeReview, name='LikeReview'),
]