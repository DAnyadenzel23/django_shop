from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product', 'section']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name_of_organization', 'created']
    fields = ['user_name', ('name_of_organization', 'tin'),
              'created', ('phone_number', 'email'), 'comment']

    readonly_fields = ('created',)
    search_fields = ('name_of_organization', 'tin')
    inlines = [OrderItemInline]

