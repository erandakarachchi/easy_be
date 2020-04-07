from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Restaurant(models.Model):
    name = models.CharField(max_length=100,default ="Sample Restaurant")
    address = models.CharField(max_length=250,default="No 12, Abc street, centrel city,NY")
    email = models.EmailField(max_length=250,default="abc@gmail.com")
    mobile = PhoneNumberField(null=False,blank=False, unique=True,default="0717878782")
    latitude = models.DecimalField( max_digits=22,decimal_places=16,default="90.12121121")
    longitude = models.DecimalField( max_digits=22,decimal_places=16,default="90.12121121")
 
class Food(models.Model):
    name = models.CharField(max_length=100)
    food_type = models.CharField(max_length =2)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name # returning the name for the food field. instead of the whole object.
    
class Customers(models.Model):
    name = models.CharField(max_length=100,default="Sample customer")
    mobile = PhoneNumberField(null=False,blank=False,unique=True,default="0887867346")
    email=models.EmailField(max_length=250,default ="abc@gmail.xyz")
    food = models.ManyToManyField(Food)
    
class Orders(models.Model):
    total = models.DecimalField(max_digits =7,decimal_places=2,default="67.00" )
    order_date = models.DateTimeField()
    customers = models.ForeignKey(Customers,on_delete=models.CASCADE)
    