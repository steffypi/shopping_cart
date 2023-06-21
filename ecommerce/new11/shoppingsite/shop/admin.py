from django.contrib import admin
from shop.models import Category,Product
# Register your models here.
class Categoryadmin(admin.ModelAdmin):
    list_display = ['name','slug',]
    prepopulated_fields={'slug':('name',)}
admin.site.register(Category,Categoryadmin)

class Productadmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price','stock','category','available','created','updated',]
    prepopulated_fields={'slug':('name',)}
admin.site.register(Product,Productadmin)