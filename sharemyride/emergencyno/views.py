from django.shortcuts import render
from emergencyno.models import Emergencynumber
# Create your views here.
def emgno (request):
    if request.method == "POST":
        ob = Emergencynumber()
        ob.name = request.POST.get('name')
        ob.emg_no = request.POST.get('number')

    return render(request,'emergencyno/emgno.html')

def viewemg (request):
    return render(request,'emergencyno/viewemgno.html')
def alert (request):
    return render(request,'emergencyno/alert.html')
