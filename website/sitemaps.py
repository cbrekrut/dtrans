from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Blog, Service

class StaticViewSitemap(Sitemap):
    changefreq = 'daily'

    def items(self):
        return ['index', 'about', 'contacts', 'services']

    def location(self, item):
        return reverse(item)

    def priority(self, item):
        if item == 'index':
            return 1.0
        return 0.8  

class BlogSitemap(Sitemap):
    priority = 0.6
    changefreq = 'weekly'

    def items(self):
        return Blog.objects.all()

    def lastmod(self, obj):
        return obj.pub_date  # Use pub_date instead of updated_at

class ServiceSitemap(Sitemap):
    priority = 0.7
    changefreq = 'weekly'

    def items(self):
        return Service.objects.all()
