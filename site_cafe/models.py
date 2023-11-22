from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=40, unique=True)
    position = models.SmallIntegerField(unique=True)
    slug = models.SlugField(max_length=40, unique=True, db_index=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Settings_Category:
        order = ('position', )

class Dish(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='url')
    position = models.PositiveSmallIntegerField()
    ingredients = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='dishes')
    is_visible = models.BooleanField(default=True)
class Reservation(models.Model):
    user_name = models.CharField(max_length=50)
    user_phone = models.CharField(max_length=15)
    user_datetime = models.DateTimeField()
    user_count = models.PositiveIntegerField()
    special_requests = models.TextField(blank=True)

    reservation_datetime = models.DateTimeField(auto_now_add=True)
    processing = models.BooleanField(default=True)
    class Meta:
        ordering = ('-reservation_datetime',)

