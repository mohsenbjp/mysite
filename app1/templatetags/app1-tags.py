from django import template
register = template.Library()
from blog.models import Post,Category

@register.inclusion_tag('app1/app1-latestpost.html')
def latestpost():
    posts=Post.objects.filter(status=1).order_by('-published_date')[0:6]
    return{'posts':posts}
