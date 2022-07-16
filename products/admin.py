from django.contrib import admin

# Register your models here.

from .models import Offer, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock']

class OfferAdmin(admin.ModelAdmin):
    list_display = ("code", "discount")

admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)
