from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField


class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True) 
    content = HTMLField()
    pub_date = models.DateTimeField('date published')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class BlogImage(models.Model):
    blog = models.ForeignKey(Blog, related_name='images', on_delete=models.CASCADE) 
    image = models.ImageField(upload_to='blog/')


class Service(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = HTMLField()
    def save(self, *args, **kwargs):
            if not self.slug:
                self.slug = slugify(self.name)
            super().save(*args, **kwargs)
    def __str__(self):
        return self.name



class ServiceImage(models.Model):
    service = models.ForeignKey(Service, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='services/')

    def __str__(self):
        return f"Image for {self.service.name}"
    
class Gallery(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class GalleryPhoto(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='gallery_photos')
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.caption