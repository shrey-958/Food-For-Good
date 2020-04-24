#from django.contrib import admin
from django.urls import path, include, re_path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup_view , name="signup"),
    path('login/', views.login_view , name="login"),
    path('logout/', views.logout_view , name="logout"),
    path('order/history/',views.order_history, name="orderhistory"),
    path('add-to-cart/<slug>/', views.add_to_cart_view, name="addtocart"),
    path('remove-from-cart/<slug>/', views.remove_from_cart_view, name="removefromcart"),
    path('order/summary/',views.order_summary, name="ordersummary"),
    path('add-item-to-cart/<slug>/', views.add_item_to_cart_view, name="additemtocart"),
    path('remove-item-from-cart/<slug>/', views.remove_item_from_cart_view, name="removeitemfromcart"),
    path('remove-full-item-from-cart/<slug>/', views.remove_full_item_from_cart_view, name="removefullitemfromcart"),
    path('order/checkout/',views.checkout, name="checkout"),
    path('profileview/',views.profileview, name="profileview"),

    
]