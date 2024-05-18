from django.db import models
from django.utils.html import format_html

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    stack = models.CharField(max_length=100, default='default_value')
    foto1 = models.ImageField(upload_to='project_images/', blank=True, null=True)  
    foto2 = models.ImageField(upload_to='project_images/', blank=True, null=True)  
    foto3 = models.ImageField(upload_to='project_images/', blank=True, null=True)  
    link = models.URLField(max_length=200, default='http://127.0.0.1:8082/')
    link_github = models.URLField(max_length=200, default='https://github.com/akbaraulia') 

    def __str__(self):
        return self.title
    
    def image_tag(self, obj):
        if obj.foto1 and obj.foto1.name and hasattr(obj.foto1, 'url'):
            return format_html('<img src="{}" width="50" height="50" />', obj.foto1.url)
        else:
            return "No Image"