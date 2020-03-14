from django.contrib import admin
from .models import File


class FileAdmin(admin.ModelAdmin):
    list_display = ['name', 'author']
    list_display_links = ['name', 'author']


admin.site.register(File, FileAdmin)
