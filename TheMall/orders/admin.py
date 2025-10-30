from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'store', 'total_amount', 'status', 'created_at')
    list_filter = ('status', 'created_at', 'store')
    search_fields = ('customer__username', 'store__name')
    inlines = [OrderItemInline]
    ordering = ('-created_at',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity', 'price_at_time')
    search_fields = ('product__name', 'order__customer__username')
