from django.contrib import admin

from app.models import Product, Image, Attribute, AttributeValue, ProductAttribute

# Register your models here.


# admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Attribute)
admin.site.register(AttributeValue)
admin.site.register(ProductAttribute)


# admin.site.unregister(Group)
# admin.site.unregister(User)


class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'discount', 'price')


admin.site.register(Product, ProductModelAdmin)
