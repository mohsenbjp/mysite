from django.urls import path
from .views import blog_home,blog_single

app_name='blog'

urlpatterns = [
    path('',blog_home,name='index'),
    path('<int:pid>',blog_single,name='single'),
    path('category/<str:cat_name>',blog_home,name='category'),
    path('author/<str:author_username>',blog_home,name='author'),
]
