from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority=0.5
    changefreq='daily'
    def items(self):
        return ['app1:index','app1:about','app1:contact']
    def location(self,item):
        return reverse(item)
