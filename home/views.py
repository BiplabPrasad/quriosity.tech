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

def activity(request):
  return render(request,'activity.html')

def dashboard(request):
  return render(request,'dashboard.html')

def faq(request):
  return render(request,'faq.html')

def profile(request):
  return render(request,'profile.html')

def settings(request):
  return render(request,'settings.html')

def logout(request):
  return render(request,'logout.html')

