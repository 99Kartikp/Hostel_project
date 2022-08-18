import http
from unicodedata import category
from django.shortcuts import render,redirect
from django.http import HttpResponse
from store.models.product import Product
from store.models.student import Student
from store.models.category import Category
from django.contrib.auth.hashers import make_password
from django.views import View

 
class Addproducts(View):
    def get(self,request):
       categories = Category.get_all_categories()
       return render(request , 'addproducts.html'  , {'categories' : categories} )

 
    def post(self,request):
        name=request.POST.get('name')
        price=request.POST.get('price')
        category_name=request.POST.get('category')
        
        category= Category.get_category_id_by_name(category_name)
        print(category)

        description=request.POST.get('description')

        if request.FILES:
            image=request.FILES['image']
        
        student = request.session.get('student')
        
        print(Category(id=category))

        product=Product(name=name,price=price,category=Category(id=category),
                        description=description,image=image,
                        student=Student(id=student))

        product.save()
        return redirect('homepage')

    
    

 