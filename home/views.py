from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
  return render(request,'dashboard.html')

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

def problems(request):
  return render(request,'problems.html')

def handleSignup(request):
  if(request.method=='POST'):
    # get the post parameters
    username = request.POST['username']
    fname = request.POST['fname']
    # mname = request.POST['mname']
    lname = request.POST['lname']
    email = request.POST['email'] 
    pass1 = request.POST['pass1']
    pass2 = request.POST['pass2']
    terms = request.POST['terms']

    # ------ validating all the user data ------
    # ------ validating fname -------
    if len(fname)>30:
      messages.error(request,"first name max lenght 30 char")
      return redirect('signup')
    if len(fname)==0:
      messages.error(request,"Enter first name")
      return redirect('signup')
    # check wheather the fname does not have any special characters
    if not fname.isalpha():
      messages.error(request,"first name should contain characters only")
      return redirect('signup')
    


    # ------ validating lname -------
    if len(lname)>30:
      messages.error(request,"last name max lenght 30 char")
      return redirect('signup')
    if len(lname)==0:
      messages.error(request,"Enter last name")
      return redirect('signup')
    # check wheather the lname does not have any special characters
    if not lname.isalpha():
      messages.error(request,"Last name should contain characters only")
      return redirect('signup')
    


    # --------- validating username -----------
    if len(username)>15:
      messages.error(request,"username max lenght 15 char")
      return redirect('signup')
    if len(username)<8:
      messages.error(request,"username min lenght 8 char")
      return redirect('signup')
    # check wheather the username is taken by some other user or not
    if not username.isalnum():
      messages.error(request,"username should be alphanumeric")
      return redirect('signup')
    


    # ------ validating email -------
    if len(email)>64:
      messages.error(request,"Email max lenght 64 char")
      return redirect('signup')
    if len(email)==0:
      messages.error(request,"Enter your email")
      return redirect('signup')
    # check wheather the email does not have any special characters


    # ------ validating pass1 -------
    if len(pass1)>24:
      messages.error(request,"Password max lenght 24 char")
      return redirect('signup')
    if len(pass1)==0:
      messages.error(request,"Enter your password")
      return redirect('signup')
    if len(pass1)<8:
      messages.error(request,"Password max lenght 8 char")
      return redirect('signup')
    # check wheather the pass1 does not have any special characters


    # ------ validating pass2 -------
    if len(pass2)>24:
      messages.error(request,"Password max lenght 24 char")
      return redirect('signup')
    if len(pass2)==0:
      messages.error(request,"Confirm your password")
      return redirect('signup')
    if pass1 != pass2:
      messages.error(request,"Passwords didn't match")
      return redirect('signup')


    # ------ validating terms -------
    if len(terms)==0:
      messages.error(request,"Please accept T&C")
      return redirect('signup')
    if terms != "True":
      messages.error(request,"Please accept the T&C")
      return redirect('signup')
    


    # Create the user
    myuser = User.objects.create_user(username,email,pass1)
    myuser.first_name = fname
    myuser.last_name = lname
    myuser.save()
    messages.success(request,"Your Account has been successfully been created")
    messages.info(request,"A verification email has been send. Please verify your account")
    return redirect('signup')
  else:
    return HttpResponse('404 - Not Found (Unauthorised access)')

