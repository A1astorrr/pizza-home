from django.contrib import admin

# Register your models here.
from goods.models import Category, Product

# admin.site.register(Category)
# admin.site.register(Product)

# для переводу русского текста в транскрипцию
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", )}
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", )}
    