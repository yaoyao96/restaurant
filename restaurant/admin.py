from django.contrib import admin

# Register your models here.
from .models import User, Restaurant, Comment, Like

admin.site.register(User)
admin.site.register(Restaurant)
admin.site.register(Comment)
admin.site.register(Like)