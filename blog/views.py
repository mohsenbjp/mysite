from django.shortcuts import render,get_object_or_404
from .models import Post,Comment
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from blog.forms import CommentForm
from django.contrib import messages
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
    if request.method =='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SECCESS,'aqa shod')
        else:
            messages.add_message(request,messages.ERROR,'aqa nashod')
    else:
        posts=get_object_or_404(Post,id=pid,status=1)
        posts.counted_views+=1
        posts.save()

        post=get_object_or_404(Post,id=pid,status=1)
        comments=Comment.objects.filter(post=post.id,approved=True).order_by('-created_date')



        #1
        # if Post.objects.filter(id=pid+1,status=1).exists():
        next_post = Post.objects.filter(id=pid+1,published_date__gt=post.published_date).order_by('published_date')
        previous_post = Post.objects.filter(id=pid-1,published_date__lt=post.published_date).order_by('published_date')


        #2
        # post=get_object_or_404(Post,id=pid,status=1)
        # post=post.filter(published_date__lte==post.published_date)






        # print(next_post.values_list('content', flat=True))
        # next_post = posts.get_next_by_published_date()
        print(next_post)
        print(previous_post)

        context={'posts':posts,'comments':comments,'next_post':next_post,'previous_post':previous_post}
        return render(request,'blog/blog-single.html',context)







def blog_search(request):
    posts=Post.objects.filter(status=1)
    if request.method=='GET':
        posts=posts.filter(content__contains=request.GET.get('s'))
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)
