from django.shortcuts import render,get_object_or_404
from .models import Post
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.utils import timezone
# import datetime
# Create your views here.
def blog_home(request,cat_name=None,author_username=None,tag_name=None):
    posts=Post.objects.filter(status=1)
    posts=posts.filter(published_date__lte=timezone.now())
    if cat_name:
        posts=posts.filter(category__name=cat_name)
    if author_username:
        posts=posts.filter(author__username=author_username)
    if tag_name:
        posts=posts.filter(tags__name__in=tag_name)

    posts=Paginator(posts,3)
    try:
        page_number=request.GET.get('page')
        posts=posts.get_page(page_number)
    except PageNotAnInteger:
        posts=posts.get_page(1)
    except EmptyPage:
        posts=posts.get_page(1)

    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)


def blog_single(request,pid):
    posts=get_object_or_404(Post,id=pid,status=1)
    posts.counted_views+=1
    posts.save()
    context={'posts':posts}
    return render(request,'blog/blog-single.html',context)

def blog_search(request):
    posts=Post.objects.filter(status=1)
    if request.method=='GET':
        posts=posts.filter(content__contains=request.GET.get('s'))
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)
