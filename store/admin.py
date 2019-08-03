from django.contrib import admin
from store.models import *


def make_init(modeladmin, request, queryset):
    queryset.update(status='Принят в обработку')
make_init.short_description = 'Пометить как принятые в обработку'

def make_end(modeladmin, request, queryset):
    queryset.update(status='Выполнен')
make_end.short_description = 'Пометить как выполненые'


class OrderAdmin(admin.ModelAdmin):
    list_filter = ['status']
    actions = [make_init, make_end]


class ProductAdmin(admin.ModelAdmin):
    list_filter = ['category']


class CategoryAdmin(admin.ModelAdmin):
    list_filter = ['parentCategory']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ParentCategory)
admin.site.register(Order, OrderAdmin)
admin.site.register(MoneyType)

# admin.site.register(CartItem)
# admin.site.register(Cart)
admin.site.register(Brand)