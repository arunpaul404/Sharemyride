from django.shortcuts import render
from complaint.models import Complaint
import datetime
# Create your views here.
def complaint (request):
    return render(request,'complaint/complaints.html')
def postcmpt (request):
    if request.method =="POST":
        ob=Complaint()
        ob.complaint=request.POST.get('complaints')
        ob.time=datetime.datetime.now()
        ob.date=datetime.date.today()
        ob.reply='pending'
        ob.user_id=1
        ob.save()
    return render(request,'complaint/postcpmlt.html')
def postrply(request):
    if request.method =="POST":
        ob=Complaint()
        ob.reply=request.POST.get('reply')
        ob.time=datetime.datetime.now()
        ob.date=datetime.date.today()
        ob.user_id=1
        ob.save()
    return render(request,'complaint/post_reply.html')
def viewrply(request):
    return render(request,'complaint/view_reply.html')
