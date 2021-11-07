from django.urls import path
from .views import about,elements,contact,index

app_name='app1'

urlpatterns = [
    path('',index,name='index'),
    path('about',about,name='about'),
    path('elements',elements,name='elements'),
    path('contact',contact,name='contact'),
]
