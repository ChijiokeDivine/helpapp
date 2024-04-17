from django.contrib.sitemaps import Sitemap
from django.db.models.base import Model
from django.urls import reverse
from .models import Blog

class StaticSitemap(Sitemap):
    def items(self):
        return ['core:index','core:about','core:contact','core:team']
    def location(self, item):
        return reverse(item)
    
class BlogSitemap(Sitemap):
    def items(self):
        return Blog.objects.all().order_by('-date')  
    
