from django.shortcuts import render
from vehicles.models import Vehicles
# Create your views here.
def mngveh(request):
    return render(request,'vehicles/mngveh.html ')
def regvehicle(request):
    if request.method == "POST":
        ob = Vehicles()
        ob.vehicle_name = request.POST.get('vehiclename')
        ob.model = request.POST.get('model')
        ob.registered_no = request.POST.get('registeredno')
        ob.type = request.POST.get('type')
        ob.user_id = 1
        ob.save()


    return render(request,'vehicles/regvehicle.html')