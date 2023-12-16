from django.db import models
from car_brand.models import Car_Brand
# Create your models here.

class Car_Model(models.Model):
    image = models.ImageField(upload_to='car_model/media/uploads/', blank = True, null = True)
    car_name = models.CharField(max_length = 30)
    car_descriptions = models.TextField()
    car_price = models.CharField(max_length = 40)
    quantity = models.IntegerField(default=0)
    brand = models.ForeignKey(Car_Brand, on_delete = models.CASCADE)

    def __str__(self):
        return self.car_name
    

class Comment(models.Model):
    post = models.ForeignKey(Car_Model, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comments by {self.name}"