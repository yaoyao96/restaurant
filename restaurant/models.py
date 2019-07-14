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

class Comment(models.Model):
    c_restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    c_user = models.ForeignKey(User, on_delete=models.CASCADE)
    c_rate = models.IntegerField(default=0)
    c_desc = models.CharField(max_length=200,null=True)
    c_date = models.DateField(default=date.today)
    def __str__(self):
        return self.c_desc

class Like(models.Model):
    l_user = models.ForeignKey(User, on_delete=models.CASCADE)
    l_comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    def __str__(self):
        return self.l_user.u_name + " / " + self.l_comment.c_desc

