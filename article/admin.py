from django.contrib import admin
from .models import *
from django.contrib.auth.models import User, Group

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(AboutUs)

@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('id', 'company', 'url', 'photo')
    list_display_links = ('id', 'company')

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(Regions)
class RegionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'region', 'user', 'status', 'date')
    list_display_links = ('id', 'title')
    list_filter = ('category', 'region', 'user', 'status')
    date_hierarchy = 'date'
