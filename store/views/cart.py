from django.shortcuts import render,redirect
from store.models.product import Product
from store.models.category import Category
from store.models.student import Student
from django.contrib.auth.hashers import check_password
from django.views import View
from store.models.product import Product


class Cart(View):
    def get(self,request):
        ids=list(request.session.get('cart').keys())
        products=Product.get_products_by_id(ids)
        print(products) 
        return render(request,'cart.html',{'products':products})


 