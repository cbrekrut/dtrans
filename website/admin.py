from django.contrib import admin
from .models import Blog, BlogImage, Service, ServiceImage, GalleryPhoto, Gallery

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
    list_display = ('name',)
    search_fields = ('name',)

class GalleryPhotoInline(admin.TabularInline):
    model = GalleryPhoto

@admin.register(Gallery)
class GaleryAdmin(admin.ModelAdmin):
    inlines = [GalleryPhotoInline]
    
    
admin.site.register(Blog, BlogAdmin)
admin.site.register(Service, ServiceAdmin)
