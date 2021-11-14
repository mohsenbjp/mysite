from django import template
register = template.Library()
from blog.models import Post

@register.inclusion_tag('blog/blog-latestpost.html')
def latestpost(a=3):
    postt=Post.objects.filter(status=1).order_by('published_date')[:a]
    return {'postt':postt}
