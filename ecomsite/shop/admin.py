from django.contrib import admin
from .models import Product,Order
# Register your models here.
admin.site.site_header = 'E-commerce Site'
admin.site.site_title = 'ABC Shopping'
admin.site.index_title = 'Manage ABC Shopping'


class ProductAdmin(admin.ModelAdmin):

    def change_category_to_default(self, request, queryset):
        queryset.update(category='default')

    change_category_to_default.short_description = 'Default Category'
    list_display = ('title', 'price',  'category', 'discountPrice', 'description')
    search_fields = ('title',)
    actions=('change_category_to_default',)
    fields =('title', 'price',)
    list_editable=('price', 'category',)
admin.site.register(Product,ProductAdmin)
admin.site.register(Order)
