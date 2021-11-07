from django.urls import path
from .views import blog_home,blog_single

app_name='blog'

urlpatterns = [
    path('',blog_home,name='index'),
    path('single',blog_single,name='single'),
]
