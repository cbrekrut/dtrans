from django.db import models
from django.utils.text import slugify


class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True) 
    subtitle = models.CharField(max_length=200, unique=False)
    content = models.TextField()
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

    def __str__(self):
        return f"Image for {self.article.title}"

class Service(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
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
    


