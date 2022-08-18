from audioop import reverse
from django.shortcuts import render,redirect
from store.models.product import Product
from store.models.category import Category
from store.models.student import Student
from django.contrib.auth.hashers import check_password
from django.views import View
from store.models.product import Product
from store.models.orders import Order
from store.middlewares.auth import auth_middleware
  

class OrderView(View):
    
    def get(self,request):
        student=request.session.get('student')
        orders=Order.get_orders_by_student(student)
         
        return render(request,'orders.html',{'orders':orders})
