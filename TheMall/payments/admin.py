from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'amount', 'method', 'status', 'transaction_id', 'created_at')
    search_fields = ('order__id', 'transaction_id')
    list_filter = ('status', 'method', 'created_at')
