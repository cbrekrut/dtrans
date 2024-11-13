from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import requests
from .models import Service, Blog, Gallery

def index(request):
    services = Service.objects.all()
    blogs = Blog.objects.all()
    return render(request, 'index.html',{'services':services, 'blogs':blogs})
def about(request):
    gallery = Gallery.objects.all()
    photos = gallery[0].gallery_photos.all()
    return render(request, 'about.html', {'photos': photos})
def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        telephone = request.POST.get('telephone')
        #похуй я сделаю вевером
    return render(request, 'contacts.html')
def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html',{'blogs':blogs})
def blog_detail(request, slug):
    blogs = Blog.objects.all()
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog_detail.html',{'blog':blog, 'blogs': blogs})
def services(request):
    services = Service.objects.all()
    page_obj = Service.objects.all()
    return render(request, 'services.html',{'services':services, 'page_obj': page_obj})
def service_detail(request, slug):
    services = Service.objects.all()
    service = get_object_or_404(Service, slug=slug)
    return render(request, 'service_detail.html',{'service':service, 'services': services})

