from django.shortcuts import render,get_object_or_404
from .models import Post
# import datetime
# Create your views here.
def blog_home(request,cat_name=None,author_username=None):
    posts=Post.objects.filter(status=1)
    if cat_name:
        posts=posts.filter(category__name=cat_name)
    if author_username:
        posts=posts.filter(author__username=author_username)

    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request,pid):
    posts=get_object_or_404(Post,id=pid,status=1)
    context={'posts':posts}
    return render(request,'blog/blog-single.html',context)
