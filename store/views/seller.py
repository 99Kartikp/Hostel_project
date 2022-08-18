from django.shortcuts import render,redirect
from store.models.product import Product
from store.models.category import Category
from store.models.student import Student
from django.contrib.auth.hashers import check_password
from django.views import View
from store.models.product import Product


class Seller(View):
   def post(self,request):
    product=request.POST.get('product')
    product=int(product)
    products=Product.get_product_by_id(product)
    return render(request,'seller.html',{'products':products})
 


 