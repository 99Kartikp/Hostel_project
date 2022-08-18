from django.contrib import admin
from django.urls import path
from .views import home,login,signup,addproducts,cart,check_out,orders ,seller,myproducts
from .middlewares.auth import auth_middleware



urlpatterns = [
    path('', home.Index.as_view(),name='homepage'),
    path('login',login.Login.as_view(),name='login'),
    path('signup',signup.Signup.as_view(),name='signup'),
    path('addproducts',addproducts.Addproducts.as_view(),name='addproducts'),
    path('logout/',login.logout,name='logout'),
    path('cart',cart.Cart.as_view(),name='cart'),
    path('check_out',auth_middleware(check_out.CheckOut.as_view()),name='check_out'),
    path('orders',auth_middleware(orders.OrderView.as_view()),name='orders'),
    path('seller',seller.Seller.as_view(),name='seller'),
    path('myproducts', myproducts.Myproducts.as_view() ,name='myproducts'),

    
]
