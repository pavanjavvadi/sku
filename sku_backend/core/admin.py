from django.contrib import admin
from sku_backend.core.models import SKU, Category, Department, Location, SubCategory


# Register your models here.
admin.site.register(SKU)
admin.site.register(Category)
admin.site.register(Department)
admin.site.register(Location)
admin.site.register(SubCategory)
