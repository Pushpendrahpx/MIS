from django.urls import path, include
from . import views
from django.contrib.auth.views import *
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from main import views
from rest_framework.urlpatterns import format_suffix_patterns


router = routers.DefaultRouter()
router.register('userinfo', views.UserInfoView)
router.register('books', views.BooksView)


urlpatterns = [
    path('', include(router.urls)),
    path('api/user/', views.json_create_user, name='json'),
    path('api/books/', views.json_create_books, name='json'),
]
