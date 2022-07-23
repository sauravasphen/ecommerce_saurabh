from django.contrib import admin

# Register your models here.
from .models import  Category, Brand, Product, CartItem

class BrandAdmin(admin.ModelAdmin):
    list_display = ["name",]
    search_fields = ["name",]
    #list_filter = []
    #readonly_fields = ["quantity",]
 
    class Meta:
        model = Brand

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name",]
    search_fields = ["name",]
    #list_filter = []
    #readonly_fields = ["quantity",]
 
    class Meta:
        model = Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ["image_tag", "name", "price", "brand", "category",]
    search_fields = ["name", "price", "brand__name", "category__name",]
    list_filter = ["brand", "category", "price"]
    #readonly_fields = ["quantity",]
 
    class Meta:
        model = Product

admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(CartItem)

