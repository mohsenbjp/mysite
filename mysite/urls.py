from django.contrib import admin
from django.urls import path,include
# from .views import home
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',home),
    # path('app1/',include('app1.urls')),
    path('',include('app1.urls')),
    path('blog/',include('blog.urls')),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
