from django.contrib import admin
from .models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    date_hierarchy='created_date'
    empty_value_display='-empty-'
    list_display=('title','counted_views','status','published_date','created_date')
    list_filter = ('title','status',)
    ordering=['-created_date']
admin.site.register(Post,PostAdmin)
