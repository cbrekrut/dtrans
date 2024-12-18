from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap, BlogSitemap, ServiceSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'blog': BlogSitemap,
    'services': ServiceSitemap,
}
urlpatterns = [
    path('', views.index,name='index'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('services', views.services, name='services'),
    path('services/<slug:slug>/', views.service_detail, name='service_detail'),
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('robots.txt', views.robots_txt, name='robots_txt'),
   
]
urlpatterns += [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

