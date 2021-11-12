from django.urls import path
from .views import blog_home,blog_single# ,test

app_name='blog'

urlpatterns = [
    path('',blog_home,name='index'),
    path('<int:pid>',blog_single,name='single'),
]
