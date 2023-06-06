from django.urls import path
from .views import *


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('register/', Register.as_view(), name='register'),
    path('register/success/', RegisterSuccess.as_view(), name='register-success'),
]