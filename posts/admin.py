from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'title',
        'user',
        'description',
        'image',
        'is_deleted',
    ]

    list_display_links = [
        'pk',
        'title',
        'user',
    ]

admin.site.register(Post, PostAdmin)