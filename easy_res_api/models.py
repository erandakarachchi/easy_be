from django.db import models
 
class Food(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length =2)
    created_at = models.DateTimeField(auto_now_add=True)