from django.shortcuts import render
from booking.models import Booking
def addbooking (request):
    if request.method == "POST":
        ob=Booking()
        ob.booking=request.POST.get('NAME')
        ob.date=request.POST.get('DATE')
        ob.time=request.POST.get('TIME')
        ob.from_id=request.POST.get('LOCATION')
        ob.to_id=request.POST.get('DESTINATION')
        ob.save()

    return render(request,'booking/addbooking.html')
def bookingrqst (request):
    return render(request,'booking/bookingrqst.html')
def bookingstatus (request):
    return render(request,'booking/bookingstatus.html')
def bookusr (request):
    return render(request,'booking/bookusr.html')