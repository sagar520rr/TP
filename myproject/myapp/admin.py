from django.contrib import admin
from .models import Category, Product
from django.utils.safestring import mark_safe


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'image_preview')
    list_filter = ('category',)
    search_fields = ('name', 'category__name')
    ordering = ('name',)

    def image_preview(self, obj):
        if obj.image:
            return mark_safe('<img src="{url}" width="100" height="100" />'.format(url=obj.image.url))
        else:
            return 'No Image'

    image_preview.short_description = 'Image Preview'

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
