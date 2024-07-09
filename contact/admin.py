from django.contrib import admin
from contact import models
# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'category',
    ordering = '-id', 
    list_filter = 'category',
    search_fields = 'id', 'first_name', 'last_name',
    list_per_page = 10
    list_max_show_all = 250
    list_display_links = 'id', 'first_name',



@admin.register(models.Category)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = 'id', 
    