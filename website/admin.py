from django.contrib import admin
from .models import Blog, BlogImage, Service, ServiceImage

class BlogImageInline(admin.TabularInline):
    model = BlogImage
    extra = 1

class BlogAdmin(admin.ModelAdmin):
    inlines = [BlogImageInline]
    prepopulated_fields = {'slug': ('title',)}  # Автоматическая генерация slug
    list_display = ('title', 'pub_date')
    search_fields = ('title',)

class ServiceImageInline(admin.TabularInline):
    model = ServiceImage
    extra = 1

class ServiceAdmin(admin.ModelAdmin):
    inlines = [ServiceImageInline]
    prepopulated_fields = {'slug': ('name',)}  # Автоматическая генерация slug
    list_display = ('name', 'price')
    search_fields = ('name',)


    
    
admin.site.register(Blog, BlogAdmin)
admin.site.register(Service, ServiceAdmin)
