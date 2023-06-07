from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('register/', Register.as_view(), name='register'),
    path('register/success/', RegisterSuccess.as_view(), name='register-success'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('create-request/', create_request, name='create_request'),
    path('request/<int:request_id>/delete/', delete_request, name='delete_request'),
    path('categories/', category_list, name='category_manager'),
    path('add-category/', add_category, name='add_category'),
    path('category/<int:request_id>/delete/', delete_category, name='delete_category'),
    path('request/<int:request_id>/change_status/', change_status, name='change_status'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

