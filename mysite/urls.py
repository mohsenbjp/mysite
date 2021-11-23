from django.contrib import admin
from django.urls import path,include
# from .views import home
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from app1.sitemaps import StaticViewSitemap
from blog.sitemaps import Blogsitemap

sitemaps = {'static':StaticViewSitemap,
            'blog':Blogsitemap
            }

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',home),
    # path('app1/',include('app1.urls')),
    path('',include('app1.urls')),
    path('blog/',include('blog.urls')),
    path('accounts/', include('allauth.urls')),
    path('sitemap.xml',sitemap,{'sitemaps':sitemaps},name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt',include('robots.urls')),
    path('summernote/',include('django_summernote.urls')),
    path('captcha/', include('captcha.urls')),

]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
