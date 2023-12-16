from django.db import models
from car_model.models import Car_Model
# Create your models here.

class Buy_car(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField()
    car = models.ForeignKey(Car_Model, on_delete = models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name