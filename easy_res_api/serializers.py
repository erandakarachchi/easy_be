from rest_framework import serializers
from easy_res_api.models import Food,Restaurant,Orders,Customers

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'
        
class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Orders
        fields="__all__"
        

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customers
        fields="__all__"