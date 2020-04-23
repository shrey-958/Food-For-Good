from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from recipe.models import Order, OrderItem, Dish
from django.http import HttpResponse
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .forms import CreateUserForm, ProfileForm

# Create your views here.
def signup_view(request):
    #form = UserCreationForm()
    if request.method == 'POST' : 
        form =  CreateUserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('recipe:list')

    else : 

        form = CreateUserForm()
        profile_form = ProfileForm()
        
    context = {'form': form, 'profile_form': profile_form}
        
    return render(request, 'accounts/signup.html', context)


def login_view(request):
    if request.method == 'POST' :
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            # log in the user
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST :
                return redirect(request.POST.get('next'))
            else :
                return redirect('recipe:list')


    else :

        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form' : form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('recipe:list')


@login_required(login_url= "/accounts/login")
def order_history(request):
    orders = Order.objects.filter(user = request.user, isOrdered=True).order_by('-date')
    
    
    

    return render(request, 'accounts/order_history.html', {'orders' : orders})


    


@login_required(login_url= "/accounts/login")
def add_to_cart_view(request,slug):
    dish = get_object_or_404(Dish, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(user=request.user, dish_name = dish, isOrdered=False)
    order_qs = Order.objects.filter(user = request.user, isOrdered = False)
    if order_qs.exists():
        order = order_qs[0]
        if order.dishes.filter(dish_name__slug = dish.slug).exists():
            order_item.quantity +=1 
            order_item.save()
            messages.info(request, 'This item quantity was updated.')
        else :
            messages.info(request, 'This item was added to your cart.')
            order.dishes.add(order_item)
    else:
        order = Order.objects.create(user = request.user)
        order.dishes.add(order_item)
        messages.info(request, 'This item was added to your cart.')
    
    return redirect("recipe:detail", slug=slug)


@login_required(login_url= "/accounts/login")
def add_item_to_cart_view(request,slug):
    dish = get_object_or_404(Dish, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(user=request.user, dish_name = dish, isOrdered=False)
    order_qs = Order.objects.filter(user = request.user, isOrdered = False)
    if order_qs.exists():
        order = order_qs[0]
        if order.dishes.filter(dish_name__slug = dish.slug).exists():
            order_item.quantity +=1 
            order_item.save()
            
        else :
           
            order.dishes.add(order_item)
    else:
        order = Order.objects.create(user = request.user)
        order.dishes.add(order_item)
        
    
    return redirect("accounts:ordersummary")


@login_required(login_url= "/accounts/login")
def remove_from_cart_view(request,slug):
    dish = get_object_or_404(Dish, slug=slug)
    order_qs = Order.objects.filter(user = request.user, isOrdered = False)
    if order_qs.exists():
        order = order_qs[0]
        if order.dishes.filter(dish_name__slug = dish.slug).exists():
            order_item = OrderItem.objects.filter(user=request.user, dish_name = dish,  isOrdered=False)[0]
            order.dishes.remove(order_item)
            messages.info(request, 'This item was removed from your cart.')
            return redirect("recipe:detail", slug=slug)
        else:
             messages.info(request, 'This item was not in your cart.')
             return redirect("recipe:detail", slug=slug)

        
            
    else : 
            messages.info(request, 'You do not have an active order.')
            return redirect("recipe:detail", slug=slug)



@login_required(login_url= "/accounts/login")
def order_summary(request):
    try:
        order = Order.objects.get(user=request.user, isOrdered = False)
        context = {'order':order}
    
    except ObjectDoesNotExist:
         
         return HttpResponse('<h1  style="text-align:center;font-family:sans-serif;">You do not have an active order :(</h1><h3 style="margin-top:5px;text-align:center;font-family:sans-serif;">Go back to menu</h3>')

    return render(request, "accounts/order_summary.html", context)


@login_required(login_url= "/accounts/login")
def remove_item_from_cart_view(request,slug):
    dish = get_object_or_404(Dish, slug=slug)
    order_qs = Order.objects.filter(user = request.user, isOrdered = False)
    if order_qs.exists():
        order = order_qs[0]
        if order.dishes.filter(dish_name__slug = dish.slug).exists():
            order_item = OrderItem.objects.filter(user=request.user, dish_name = dish,  isOrdered=False)[0]
            if order_item.quantity>1:
                order_item.quantity -=1 
            else :
                 order.dishes.remove(order_item)
            order_item.save()
            
           
            return redirect("accounts:ordersummary")
        else:
             messages.info(request, 'This item was not in your cart.')
             return redirect("recipe:detail", slug=slug)

        
            
    else : 
            messages.info(request, 'You do not have an active order.')
            return redirect("recipe:detail", slug=slug)


@login_required(login_url= "/accounts/login")
def remove_full_item_from_cart_view(request,slug):
    dish = get_object_or_404(Dish, slug=slug)
    order_qs = Order.objects.filter(user = request.user, isOrdered = False)
    if order_qs.exists():
        order = order_qs[0]
        if order.dishes.filter(dish_name__slug = dish.slug).exists():
            order_item = OrderItem.objects.filter(user=request.user, dish_name = dish,  isOrdered=False)[0]
            order.dishes.remove(order_item)
           
            return redirect("accounts:ordersummary")
        else:
            
             return redirect("accounts:ordersummary")

        
            
    else : 
            
            return redirect("accounts:ordersummary")




@login_required(login_url= "/accounts/login")
def checkout(request):
     order_qs = Order.objects.filter(user = request.user, isOrdered = False)
     if order_qs.exists():
         for order_item in order_qs:
             order_item.isOrdered = True
             order_item.save()
        
         order_qs.isOrdered=True
         order_qs.update()

     return render(request, "accounts/checkout.html")


    


