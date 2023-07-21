from django.shortcuts import render,redirect
from PGApp import models
from django.contrib import messages as msg

# Create your views here.

def login(request):
    return render(request, 'login.html')

def signin(request):
    return render(request, 'signin.html')

def home(request):
    return render(request, 'home.html')

def viewRoom(request):
    room = models.room.objects.all()

    return render(request, 'viewRoom.html', {'rooms':room})


def adminportal(request):
    return render(request, 'admin.html')

def SigninForm(request):
    if request.method=='POST':
        uname = request.POST['uname']
        contactno = request.POST['contactno']
        emaliid = request.POST['emaliid']
        psw = request.POST['psw']

        user = models.users(username=uname, phno=contactno, email=emaliid, password=psw)
        user.save()

        return redirect(home)
    
def loginForm(request):
    if request.method=='POST':
        uname = request.POST['uname']
        psw = request.POST['psw']

        if uname == 'admin@pg.com' and psw=='admin':
            return redirect(adminportal)
        user = models.users.objects.all()
        for s in user:
            if s.email==uname and s.password==psw:
                return redirect(home)
        msg.warning(request, "Please insert valid Details!!!")
        return redirect("/")

def viewUsers(request):
    user = models.users.objects.all()

    return render(request, 'viewUsers.html', {'users':user})

def addRoom(request):
    return render(request, 'addRoom.html')

def addRoomForm(request):
    if request.method == 'POST':
        roomname = request.POST['roomname']
        roomno = request.POST['roomno']
        capacity = request.POST['capacity']
        rent = request.POST['rent']
        desc = request.POST['desc']

        room = models.room(room_name=roomname, room_no=roomno, cap=capacity, rent_room=rent, description=desc)
        room.save()

        return redirect(adminportal)

def bookingrooms(request, num):
    room = models.room.objects.filter(id=num)
    
    return render(request, 'bookingrooms.html', {'rooms':room})

def bookingForm(request):
    if request.method=='POST':
        username = request.POST['username']
        roomname = request.POST['roomname']
        roomno = request.POST['roomno']
        capacity = request.POST['capacity']
        rent = request.POST['rent'] 
        desc = request.POST['desc']

        book = models.bookingrooms(booked_user=username, booked_room_name=roomname, booked_room_no=roomno, booked_cap=capacity, booked_rent_room=rent, booked_description=desc)
        book.save()

        return redirect(home)

def bookedrooms(request):
    book = models.bookingrooms.objects.all()

    return render(request, 'bookedrooms.html', {'book':book})
        