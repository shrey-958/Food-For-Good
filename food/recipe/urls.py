from django.urls import path,re_path
from . import views

app_name = 'recipe'

urlpatterns = [
    path('menu/', views.menu_list, name="list"),
     path('buy/', views.buy_food, name="buy"),
    re_path('(?P<slug>[\w-]+)/$', views.menu_detail, name="detail"),
]