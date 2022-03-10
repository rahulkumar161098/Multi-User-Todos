from django.contrib import admin
from .models import Customer, Product, Todo

# Register your models here.

class ProductViews(admin.ModelAdmin):
    list_display=('p_tag_line','p_price','p_selling_price','p_discount','user')
admin.site.register(Product, ProductViews)

class CustomerViews(admin.ModelAdmin):
    list_display=('name','number','state','zip_code','user')
admin.site.register(Customer, CustomerViews)

class TodoViews(admin.ModelAdmin):
    list_display= ('title', 'user', 'created_at')
admin.site.register(Todo, TodoViews)