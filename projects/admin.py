from django.contrib import admin
from .models import Project
from django.utils.html import format_html

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'stack', 'image_tag', 'link', 'link_github')
    list_filter = ('stack',)  
    search_fields = ('title', 'stack') 

    def image_tag(self, obj):
        if obj.foto1 and hasattr(obj.foto1, 'url'):
            return format_html('<img src="{}" width="50" height="50" />', obj.foto1.url)
        else:
            return "No Image"
    image_tag.short_description = 'Foto 1'
    
admin.site.register(Project, ProjectAdmin)