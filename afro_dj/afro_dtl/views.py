from django.shortcuts import render

# Create your views here.
def index(request):
    pr_title = 'Afro-Django'
    return render(request, 'index.html', {'pr_title': pr_title})