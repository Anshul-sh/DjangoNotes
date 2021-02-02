url.py 

from django.contrib import admin
from django.urls import path
from my_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns = [
 path(r'', views.cars_by_owner, name='cars_by_owner'),
 ]
 
views.py

from django.shortcuts import render

# Create your views here.
def cars_by_owner(request, owner_name){
    car_list = Car.objects.get(car=owner_name)
    response = HttpResponse()
    for car in cars_list.all():
    para = '<p>' + str(car.modelname) +'  '+ str(car.year) + '</p>'
    response.write(para)
    return response
}