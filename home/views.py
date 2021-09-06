from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  return HttpResponse("Hello, Cool IT Help!")

def base(request):
  return render(request,'base.html')

def base_copy(request):
  return render(request,'base_copy.html')

def signup(request):
  return render(request,'signup.html')

def login(request):
  return render(request,'login.html')

