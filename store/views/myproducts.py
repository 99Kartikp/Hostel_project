from email.mime import image
from itertools import product
from django.shortcuts import render , redirect
from django.contrib.auth.hashers import  check_password
from store.models.student import Student
from store.models.category import Category
# from store.models.userproducts import UserProducts
from django.views import  View
from store.models.product import  Product
from django.core.files.storage import FileSystemStorage
from store.models.orders import Order

 

class Myproducts(View):
    def get(self ,request):
        student=request.session.get('student')
        products = Product.get_products_by_student(student)
        print(products)
        return render(request , 'myproducts.html' , {'products' : products} )


    def post(self ,request):
          product_id=request.POST.get('product')
          Product.delete_product_by_id(product_id)
          student=request.session.get('student')
          products = Product.get_products_by_student(student)
          return render(request , 'myproducts.html' , {'products' : products} )

           
         
   

     