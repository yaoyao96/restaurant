from django.urls import path

from . import views

app_name = 'restaurant'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # ex: /restaurant/5/
    path('<int:restaurant_id>/', views.detail, name='detail'),
    # ex: /restaurant/5/review
    path('<int:pk>/review/', views.ReviewView.as_view(), name='review'),
    # ex: /restaurant/5/submitreview
    path('<int:restaurant_id>/submitreview/', views.SubmitReview, name='SubmitReview'),
    # ex: /restaurant/5/likereview
    path('<int:restaurant_id>/<int:review_id>/likereview/', views.LikeReview, name='LikeReview'),
    # ex: /restaurant/5/comment
    path('<int:review_id>/comment/', views.comment, name='comment'),
    # ex: /restaurant/5/submitcomment
    path('<int:review_id>/submitcomment/', views.SubmitComment, name='SubmitComment'),
    # ex: /restaurant/5/reply
    path('<int:comment_id>/reply/', views.reply, name='reply'),
    # ex: /restaurant/5/submitreply
    path('<int:review_id>/submitreply/', views.SubmitReply, name='SubmitReply'),
    
]