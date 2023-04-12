from django.shortcuts import render

# Create your views here.
def index(request):
    pr_title = 'Afro-Django'
    username = 'Mariam'
    gender = 'Male'
    return render(
        request,
        'index.html', 
        {'pr_title': pr_title, 'username':username, 'gender':gender}
    )