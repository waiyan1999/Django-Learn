from django.contrib import admin
from api.models import Category,Product,Cart,CartItem

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
