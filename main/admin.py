from django.contrib import admin
from .models import PostImage

# Register your models here.

admin.site.site_title = "Pinterest Admin Panel"
admin.site.site_header = "Pinterest Admin Panel"
admin.site.index_title = "Welcome to the admin panel of Pinterest"

admin.site.register(PostImage)
