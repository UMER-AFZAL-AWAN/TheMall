from django.contrib import admin
from .models import Product, Inventory

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'store', 'price', 'category', 'created_at')
    search_fields = ('name', 'store__name')
    list_filter = ('store', 'category')
    ordering = ('-created_at',)

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'quantity', 'updated_at')
    search_fields = ('product__name',)
    list_filter = ('updated_at',)
