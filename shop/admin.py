from django.contrib import admin
from .models import Product,Contact


admin.site.register(Product)
admin.site.register(Contact)

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['product_id','product_name','category', 'description','image', 'pub_date']
#     search_fields = ('product_name',)


