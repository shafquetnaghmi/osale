from django.contrib import admin
from .models import Product,CategoryModel,FeaturedProduct

@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['unique_id','category','image','available']
    list_filter=['unique_id']

@admin.register(FeaturedProduct)
class FeaturedProductAdmin(admin.ModelAdmin):
    list_display=['product']
