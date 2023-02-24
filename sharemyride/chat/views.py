from django.shortcuts import render
from chat.models import Chat
# Create your views here.
def chat (request):
    if request.method == "POST":
        ob = Chat()
        ob.chat = request.POST.get('CHAT')
        ob.to_id=1
        ob.from_id=2
        ob.save()
    return render(request,'chat/chat.html')