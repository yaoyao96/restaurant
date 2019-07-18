from django.contrib import admin

# Register your models here.
from .models import User, Restaurant, Comment, Review

admin.site.register(User)
admin.site.register(Restaurant)
admin.site.register(Review)
admin.site.register(Comment)