import datetime
from django.db import models
from django.utils import timezone
from datetime import date

# Create your models here.
class Restaurant(models.Model):
    r_name = models.CharField(max_length=50)
    r_address = models.CharField(max_length=200)
    def __str__(self):
        return self.r_name

class User(models.Model):
    u_name = models.CharField(max_length=30)
    def __str__(self):
        return self.u_name

class Review(models.Model):
    r_restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    r_user = models.ForeignKey(User, on_delete=models.CASCADE)
    r_rate = models.IntegerField(default=0)
    r_desc = models.CharField(max_length=200,null=True)
    r_date = models.DateField(default=date.today)
    r_like = models.IntegerField(default=0)
    r_reply = models.IntegerField(null=True)
    def __str__(self):
        return self.r_desc

class Comment(models.Model):
    c_user = models.ForeignKey(User, on_delete=models.CASCADE)
    c_review = models.ForeignKey(Review, on_delete=models.CASCADE)
    c_reply_user = models.CharField(max_length=30, null=True)
    c_desc = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.c_desc

# class Like(models.Model):
#     l_user = models.ForeignKey(User, on_delete=models.CASCADE)
#     l_comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
#     def __str__(self):
#         return self.l_user.u_name + " / " + self.l_comment.c_desc

