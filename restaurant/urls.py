from django.urls import path

from . import views

app_name = 'restaurant'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # ex: /restaurant/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /restaurant/5/comment
    path('<int:pk>/comment/', views.CommentView.as_view(), name='comment'),
    # ex: /restaurant/5/submitcomment
    path('<int:restaurant_id>/submitcomment/', views.SubmitComment, name='SubmitComment'),
]