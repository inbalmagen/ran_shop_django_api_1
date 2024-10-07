from django.contrib import admin
from products.models import Cart, Category, Product

class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'total_price')
    filter_horizontal = ('products',)
    readonly_fields = ('total_price',)

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Cart, CartAdmin)