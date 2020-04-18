from django.shortcuts import render
from django.http import HttpResponse
from .models import Dish
from django.contrib.auth.decorators import login_required

# Create your views here.
def menu_list(request):
    dishes = Dish.objects.all().order_by('price')
    context = {'dishes' : dishes}
    return render(request, 'recipe/menu.html', context)

def menu_detail(request, slug):
    dish = Dish.objects.get(slug = slug)
    context = {'dish' : dish}
    return render(request, 'recipe/menu_detail.html', context)

@login_required(login_url= "/accounts/login")
def buy_food(request):
    return render(request, 'recipe/buy_food.html')
