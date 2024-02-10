from django.contrib import admin
from .models import Category, News, Contact


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'published_time', 'status')
    list_filter = ('category', 'created_time', 'published_time', 'status')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_time'
    ordering = ('status', 'published_time')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'created_time')
    search_fields = ('name', 'email', 'phone', 'subject')
    date_hierarchy = 'created_time'
    ordering = ('created_time',)
