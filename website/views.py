from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import requests
from .models import Service, Blog

def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contacts(request):
    return render(request, 'contacts.html')
def blog(request):
    blogs = BLog.objects.all()
    return render(request, 'blog.html',{'blogs':blog})
def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog_detail.html',{'blog':blog})
def services(request):
    services = Service.objects.all()
    return render(request, 'services.html',{'services':services})
def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    return render(request, 'service_detail.html',{'service':service})