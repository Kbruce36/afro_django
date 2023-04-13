from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def index(request):
    pr_title = 'Afro-Django'
    username = 'Mariam'
    gender = 'Female'
    return render(
        request,
        'index.html', 
        {'pr_title': pr_title, 'username':username, 'gender':gender}
    )

def register(request):

    return render(request, 'register.html')

def registration(request):
    if request == 'POST':
        name = request.POST.get['username']
        email = request.POST.get['email']
        password = request.POST.get['password']
        gender = request.POST.get['gender']
        user_details=[
            name,email,password,gender
        ]
        print(user_details)
    else:
        pass


   