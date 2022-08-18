from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.student import Student
from .models.orders import Order

class AdminProduct(admin.ModelAdmin):
    list_display= ['name','price','category','description']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

class AdminStudent(admin.ModelAdmin):
    list_display = ['name','branch','hostel_name','room_no','phone_no','email','password','image']

class AdminOrder(admin.ModelAdmin):
    list_display = ['product','student','quantity','price','address','phone','date']

# Register your models here.
admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Student,AdminStudent)
admin.site.register(Order,AdminOrder)
