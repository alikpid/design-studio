from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('register/', Register.as_view(), name='register'),
    path('register/success/', RegisterSuccess.as_view(), name='register-success'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('create-request/', create_request, name='create_request'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
