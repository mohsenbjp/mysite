from django.shortcuts import render,get_object_or_404
from .models import Post
import datetime
# Create your views here.
def blog_home(request):
    posts=Post.objects.filter(status=1)
    current=datetime.datetime.now()
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request,pid):
    posts=get_object_or_404(Post,id=pid,status=1)
    num_post = Post.objects.filter(author=request.user).count()
    context={'posts':posts,'num_post':num_post}
    return render(request,'blog/blog-single.html',context)

# def test(request,pid):
#     posts=get_object_or_404(Post,id=pid)
#     context={'posts':posts,'time':time}
#     return render (request,'test.html',context)
