from django.shortcuts import render
from .models import Restaurant

# Create your views here.
def homepage_view(request):
    try:
        restaurant = Restaurant.objects.first()
        restaurant_name = restaurant.name if restaurant else "Default Restaurant"
    except Restaurant.DoesNotExist:
        restaurant_name = 'Default Restaurant'
    return render(request,'homepage.html',{'restaurant_name': restaurant_name})