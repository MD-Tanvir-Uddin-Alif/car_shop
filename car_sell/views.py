from django.shortcuts import render
from car_model.models import Car_Model
from car_brand.models import Car_Brand

def home(request, Brand_slug = None):
    data = Car_Model.objects.all()
    if Brand_slug is not None:
        brand = Car_Brand.objects.get(slug = Brand_slug)
        data = Car_Model.objects.filter(brand = brand)
    brands = Car_Brand.objects.all()
    return render(request,'home.html',{'data':data, 'brand':brands})