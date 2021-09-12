from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from home.models import problem, topic
from django.core.mail import send_mail


# HTML pages
def index(request):
  return render(request,'dashboard.html')

def base(request):
  return render(request,'base.html')

def base_copy(request):
  return render(request,'base_copy.html')

def signup(request):
  return render(request,'signup.html')

def log_in(request):
  return render(request,'login.html')

def activity(request):
  return render(request,'activity.html')

def dashboard(request):
  alltopic = topic.objects.all()
  # print(alltopic)
  context = {'alltopic':alltopic}
  return render(request,'dashboard.html',context)

def faq(request):
  return render(request,'faq.html')

def profile(request):
  return render(request,'profile.html')

def settings(request):
  return render(request,'settings.html')

def search(request):
  return render(request,'search.html')

def page404(request):
  return render(request,'404.html')

def problems(request,slug):
  top = topic.objects.filter(slug=slug).first()
  prob = problem.objects.filter(topic=top).all()
  # print(top)
  # print(prob)
  context = {'top':top,'prob':prob}
  messages.info(request,"Topic --> "+top.title)
  return render(request,'problems.html',context)

# Authentication APIs
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
    if User.objects.filter(username=username).exists():
      messages.error(request,"username already taken")
      return redirect('signup')
    


    # ------ validating email -------
    if len(email)>64:
      messages.error(request,"Email max lenght 64 char")
      return redirect('signup')
    if len(email)==0:
      messages.error(request,"Enter your email")
      return redirect('signup')
    # check wheather the email does not have any special characters
    if User.objects.filter(email=email).exists():
      messages.error(request,"Account with this email already exists")
      return redirect('signup')



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
    messages.success(request,"Your Account has been successfully created")
    messages.info(request,"A verification email has been send. Please verify your account")
    return redirect('signup')
  else:
    # return HttpResponse('404 - Not Found (Unauthorised access)')
    return render(request,'404.html')

def handleLogin(request):
  if request.method == 'POST':
    #get the post parameters
    loginusername = request.POST['loginusername']
    # loginemail = request.POST['loginemail']
    loginpass = request.POST['loginpass']
    # loginrem = request.POST['loginrem']
    loginrem = request.POST.get('loginrem', 'False')

    # validating all the data from the login form
    if len(loginusername)==0:
      messages.error(request,"Enter Username")
      return redirect('login')

    if not loginusername.isalnum():
      messages.error(request,"username should be alphanumeric")
      return redirect('login')

    if len(loginpass)==0:
      messages.error(request,"Enter Password")
      return redirect('login')

    # validating the user by username and password
    user = authenticate(username = loginusername, password = loginpass)
    if user is not None:
      login(request, user)
      messages.success(request,"Successfully Logged In")
      return redirect('dashboard')
    else:
      messages.error(request,"Invalid Credentials, try again")
      return redirect('log_in')
  else:
    return render(request,'404.html')

# for logging out of the system (handleLogin)
def log_out(request):
  logout(request)
  messages.success(request,"Successfully Logged Out")
  return redirect('log_in')

def sendEmail(request):
  # I will send the email here
  send_mail(
    'Subject Test',
    'Here is the test message.',
    'support@quriosity.tech',
    ['quriosity.tech@gmail.com'],
    fail_silently=False,
  )
  return render(request,'email.html')