from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mainpage(request):
    return render(request, "loginpage/index.html")

def login(request):
    return render(request, "loginpage/loginweb.html")