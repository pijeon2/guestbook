from django.shortcuts import render, redirect
from .models import Message
# Create your views here.
def guestbook(r):
    message = Message.objects
    return render(r, 'home.html',{'message':message})

def submit(r):
    m =Message()
    m.name = r.GET['irum']
    m.email = r.GET['email']
    m.title = r.GET['title']
    m.date = r.GET['date']
    m.content = r.GET['content']
    m.pwd = r.GET['pwd']
    m.save()
    return redirect('/')