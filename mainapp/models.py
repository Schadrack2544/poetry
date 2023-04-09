from django.db import models
from ckeditor.fields import RichTextField 

class PoetryPost(models.Model):
    CATEGORY_CHOICES = [
        ('Poetry', 'Poetry'),
        ('Opinion', 'Opinion'),
        ('Short-Story', 'Short-Story'),
        ('Photography', 'Photography'),
    ]
    
    title = models.CharField(max_length=200)
    text = RichTextField()
    image = models.ImageField(upload_to='poetry_images/')
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES)
    date_posted=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class PhotographyPost(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    main_image = models.ImageField(upload_to='photography_images/')
    featured_images = models.ManyToManyField('FeaturedImage')
    date_posted=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class FeaturedImage(models.Model):
    image = models.ImageField(upload_to='photography_images/')
    date_posted=models.DateTimeField(auto_now_add=True)
