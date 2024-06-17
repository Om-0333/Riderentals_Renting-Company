from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from .models import Booking 

def home(request):
    return render(request, 'home.html')
def home2(request):
    return render(request, 'home2.html')
def process_page(request):
    return render(request, 'process.html')
def process2_page(request):
    if request.method == 'POST':
        # Retrieve form data
        name = request.POST.get('Your name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        pick_up_date = request.POST.get('pick-up-date')
        place = request.POST.get('place')
        
        # Create a new Booking object and save it to the database
        booking = Booking(name=name, mobile=mobile, email=email, pick_up_date=pick_up_date, place=place)
        booking.save()
        
        # Redirect to success page or any other page
        return redirect('success/')  

    return render(request, 'process2.html')


    
def in_page(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect homepage
            return render(request, 'index.html') 
            
        
        else:
            # Return an error message or render the login page again with an error message
            messages.error(request,"Your Username or password is wrong" )

    
    return render(request, 'in.html')
    
def up_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        name= request.POST['name']
        email = request.POST['email']

        if User.objects.filter(username=username):
            messages.error(request,"Username already exists Please try another username")
            return render(request, 'up.html')
        if User.objects.filter(email=email):
            messages.error(request,"Email already exists Please try another email")
            return render(request, 'up.html')

        myuser=User.objects.create_user(username,email,password)
        myuser.first_name=name
        myuser.save()
        messages.success(request,"Your account has been successfully created")

        return render(request, 'in.html')




    return render(request, 'up.html')


def index_page(request):
    return render(request, 'index.html')
def success_page(request):
    return render(request, 'success.html')

