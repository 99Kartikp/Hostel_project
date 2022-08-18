from django.shortcuts import render,redirect
from store.models.product import Product
from store.models.category import Category
from store.models.student import Student
from django.contrib.auth.hashers import check_password
from django.views import View
from store.models.product import Product
from store.models.orders import Order

class CheckOut(View):
    def get(self,request):
        return redirect('cart')

    def post(self,request):
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        student=request.session.get('student')
        cart=request.session.get('cart')
        products=Product.get_products_by_id(list(cart.keys()))
        print(address,phone,student,cart,products)
        
        for product in products:
            order=Order(student=Student(id = student),
                       product=product,
                       price=product.price,
                       quantity=cart.get(str(product.id)),
                       address=address,
                       phone=phone)
            order.save()
            

        request.session['cart']={}
        


        return redirect('cart')

 