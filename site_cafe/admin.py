from django.contrib import admin
from .models import Category, Dish


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Dish)
class AdminDish(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display_links = ('id', 'name')
    list_display = ('id', 'name', 'category', 'position', 'price', 'is_visible')
    list_editable = ('category', 'position', 'price', 'is_visible')
    list_filter = ('category', 'price')
    search_fields = ('name', )
