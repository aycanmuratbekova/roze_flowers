from django.contrib import admin

from payments.models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['id', 'amount', 'description', 'payment_dt', 'payment_success']
    list_filter = ['amount', 'payment_dt', 'payment_success']
    search_fields = ['amount', 'description']

