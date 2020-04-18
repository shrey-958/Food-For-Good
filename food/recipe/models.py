from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Dish(models.Model):
    SWEET = 'SW'
    SPICY = 'SP'
    SOUR = 'SO'
    BITTER = 'BT'
    TASTE_CHOICES = (
        ('SWEET', 'Sweet'),
        ('SPICY', 'Spicy'),
        ('SOUR', 'Sour'),
        ('BITTER', 'Bitter'),
    )
    INDIAN = 'INDIAN'
    ASIAN = 'ASIAN'
    ITALIAN = 'ITALIAN'
    MEXICAN = 'MEXICAN'
    SPANISH = 'SPANISH'
    JAPENESE = 'JAPANESE'
    THAI = 'THAI'
    CHINESE = 'CHINESE'
    FRENCH = 'FRENCH'
    CUISINE_CHOICES = (
        (INDIAN , 'Indian'),
        (ASIAN, 'Asian'),
        (ITALIAN, 'Italian'),
        (MEXICAN, 'Mexican'),
        (SPANISH, 'Spanish'),
        (JAPENESE, 'Japenese'),
        (THAI, 'Thai'),
        (CHINESE, 'Chinese'),
        (FRENCH, 'French')
    )
    title = models.CharField(max_length=100)
    

    slug = models.SlugField()
    taste = models.CharField(max_length=10,choices=TASTE_CHOICES, blank=True)
    cuisine = models.CharField(max_length=10,choices=CUISINE_CHOICES, blank=True)
    isVeg =  models.BooleanField(default=False)
    ingredients = models.TextField()
    frecipe = models.TextField()
    price = models.FloatField(default=500.0)
    image = models.ImageField(default="", blank=True )

    

    def __str__(self):
        return self.title


class OrderItem(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, default = None)
    dish_name = models.ForeignKey(Dish, on_delete=models.CASCADE, default = None)
    isOrdered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)
    def __str__(self):
        return self.dish_name.title
    def cost(self):
        return self.quantity*self.dish_name.price
    def item_detail(self):
        return '{0}-{1}'.format(self.dish_name, self.quantity)
    


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default = None)
    dishes = models.ManyToManyField(OrderItem)
    date = models.DateTimeField(auto_now_add = True)
    isOrdered = models.BooleanField(default=False)
    isDelivered = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username
    def total(self):
        bill=0
        for dish in self.dishes.all():
            bill += dish.cost()
        return bill





