from django.urls import path, include
from . import views

app_name = 'pages'
urlpatterns = [
   
    path('', views.landing_page, name = 'landingpage'),
]