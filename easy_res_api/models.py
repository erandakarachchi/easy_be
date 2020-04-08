from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


#if failed to apply migrations please refer to https://stackoverflow.com/a/41032590/7704650
'''
[*]run python manage.py makemigrations authentication - because when using AUTH_USER_MODEL it will replace the migration of auth_user table of django.contrib.auth altering the migration process. Thus if we fail to provide migration file for authentication app migration will no doubt fails.
[*]run python manage.py migrate.
'''
class RestaurantAdminManager(BaseUserManager):
    def create_user(self,email,date_of_birth,password=None):
        if not email:
            raise ValueError("Restaurant admin must have an email")
        user = self.model(
            email = self.normalize_email(email), #convert all chars to lowercase.
            date_of_birth = date_of_birth
        )
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self,email,date_of_birth,password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            date_of_birth = date_of_birth,
            password = password,
        )
        user.is_admin = True
        user.is_superuser = True
        
        user.save(using =self._db)
        
        return user

class RestaurantAdmin(AbstractBaseUser):
    email = models.EmailField(verbose_name ="Email Address",max_length = 150,unique=True)
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin =models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']
    
    objects = RestaurantAdminManager()

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return True
    
    def has_module_perms(self,app_lable):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin
    
    
    
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
    