from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import User_account, User_form_model, ChatBox
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import User_form
# Create your views here.
def index(request):
    pr_title = 'Afro-Django'
    if request.user.is_authenticated:
        username = request.user.username
        return render(
            request,
            'index.html', 
            {'pr_title': pr_title, 'username':username}
        )
    else:
        author = 'Bruce'
        gender = 'Male'
        return render(
            request,
            'index.html', 
            {'pr_title': pr_title, 'author':author, 'gender':gender}
        ) 
        

def register(request):

    return render(request, 'register.html')

def registration(request):
    user_name = request.POST['username']
    email = request.POST['user_email']
    password = request.POST['password']
    gender = request.POST['gender']
    user_details=[
            user_name,email,password,gender
        ]
    print(user_details)
    if User.objects.filter(username=user_name).first():
        print('Username already exists.')
        return render(request, 'login.html')
    else:
        user=User.objects.create_user(user_name, email, password)
        return render(request, 'login.html')


def login_user(request):
    #here we handle data being posted from the login form
    user_name = request.POST['username']
    pwd = request.POST['password']
    #we check if the user already has an account in te database
    if User.objects.filter(username=user_name):
        print("This username exists.")
        #if the account exists we login using the username and password fields
        logged_user = authenticate(request, username=user_name, password=pwd)
        if logged_user is not None:
            #here we are logging in the user
            auth_login(request, logged_user)
            print(user_name+" "+"Logged in successfuly")
            messages.success(request, 'You have logged in successfully. Welcome!')
            return redirect('index')
        else: 
            #here we handle a scenario where the authentication has failed
            return render(request, 'login.html')
    else:
        print("User Credentials do not exist.")
        return render(request, 'login.html')
    
def login_page(request):

    return render(request, 'login.html')

@login_required
def logout_user(request):
    auth_logout(request)
    messages.error(request, 'You have logged out successfully. Goodbye!')
    return redirect('login_page')

#test view

def user_form(request):    
    form = User_form(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
        else:
            messages.success(request, "there was an error in your submission.")
            return redirect('user_form')
        messages.success(request, ("your form has been submitted successfully."))  
        #always remember to redirect to a view that handles the page and not the page
        return redirect('userforminfo')
    else:
        return render(request, 'userform.html', {'form':form})
    
def userforminfo(request):
    all_users = User_form_model.objects.all()
    return render(request, 'userforminfo.html', {'all':all_users})


#new message view
def capture_message(request):
    messenger_field = request.POST['messenger']
    message_field = request.POST['message']
    #we are telling our model what fields to store
    #the model column = the variable 
    captured_message = ChatBox(messenger=messenger_field, message=message_field)
    #whatever has been capturd is saved within the database using the function below
    captured_message.save()
    #here we are retrieving the data saved in the model
    chats = ChatBox.objects.all()
    return render(request, 'chatbox.html', {'chats':chats})