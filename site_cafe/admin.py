from django.contrib import admin
from .models import Category, Dish, Reservation

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

@admin.register(Reservation)
class AdminReservation(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'user_phone', 'user_datetime', 'user_count', 'special_requests', 'reservation_datetime', 'processing')
    list_display_links = ('id', 'user_name')
    list_editable = ('user_phone', 'user_count', 'special_requests', 'processing')
    list_filter = ('processing', 'user_datetime')
    search_fields = ('user_name', 'user_phone', 'special_requests')
    ordering = ('-reservation_datetime',)

    def get_form(self, request, obj=None, **kwargs):
        return super(AdminReservation, self).get_form(request, obj, **kwargs)

