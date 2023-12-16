from django.contrib import admin
from .import models
# Register your models here.

class Car_Brand_Admin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('model_name',)}
    list_display = ['model_name', 'slug']


admin.site.register(models.Car_Brand, Car_Brand_Admin)
