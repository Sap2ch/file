from django.contrib import admin
from .models import *


class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'content', 'photo', 'time_create', 'is_published', 'cat')
    list_display_links = ('id', 'title', 'slug')
    search_fields = ('title', 'pk')
    list_editable = ('is_published',)
    list_filter = ('time_create', 'is_published', 'cat')
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'bio', 'photo')
    list_display_links = ('id', 'user')
    search_fields = ('user', 'pk')


admin.site.register(Posts, PostsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Profile, ProfileAdmin)
