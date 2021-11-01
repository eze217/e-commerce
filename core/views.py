from django.shortcuts import render

# Create your views here.

def home (request):
    return render(request,'core/index.html',{})

#@login_request
def login(request):
    return render(request, 'core/login.html', {})
