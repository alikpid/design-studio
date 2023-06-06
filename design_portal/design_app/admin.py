from django.contrib import admin
from .models import User, Category, Request

User = User

admin.site.register(User)

Categories = Category
admin.site.register(Categories)

Requests = Request
admin.site.register(Requests)


