from django.shortcuts import render
from user.models import User
# Create your views here.
# Create your views here.
def avlusr(request):
    return render(request,'user/avlusr.html ')
def mnguser(request):
    return render(request,'user/mnguser.html ')
def regusr(request):
    if request.method == "POST":
        ob=User()
        ob.name=request.POST.get('name')
        ob.address=request.POST.get('address')
        ob.gender=request.POST.get('gender')
        ob.phone=request.POST.get('phone')
        ob.email=request.POST.get('email')
        ob.license=request.POST.get('license')
        ob.age=request.POST.get('age')
        ob.username=request.POST.get('username')
        ob.password=request.POST.get('password')
        ob.save()

    return render(request,'user/regusr.html ')
