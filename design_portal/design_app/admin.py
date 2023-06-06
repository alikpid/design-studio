from django.contrib import admin
from .models import User

User = User

admin.site.register(User)
