from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from home.models import problem, topic, userProblemData, myfaq, account_verification, like
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404 
import json

# HTML pages
def index(request):
  # return render(request,'dashboard.html')
  return redirect('dashboard')

def base(request):
  at = topic.objects.all()
  # print(at)
  context={'at':at}
  return render(request,'base.html',context)

def base_copy(request):
  return render(request,'base_copy.html')

def signup(request):
  return render(request,'signup.html')

def log_in(request):
  return render(request,'login.html')

def activity(request):
  alltopic = topic.objects.all()
  prob = userProblemData.objects.filter(user=request.user).all().order_by('-last_updated_at')
  context = {'alltopic':alltopic,'prob':prob}
  return render(request,'activity.html',context)

def dashboard(request):
  alltopic = topic.objects.all().order_by('priority')
  # print(alltopic)
  context = {'alltopic':alltopic}
  return render(request,'dashboard.html',context)

def faq(request):
  alltopic = topic.objects.all()
  allfaq = myfaq.objects.all()
  print(allfaq)
  context = {'alltopic':alltopic, 'allfaq':allfaq}
  return render(request,'faqs.html',context)

def profile(request):
  return render(request,'profile.html')

def settings(request):
  return render(request,'settings.html')

def search(request):
  return render(request,'search.html')

def page404(request):
  return render(request,'404.html')

def problems(request,slug):
  if request.user.id == None:
    messages.warning(request,"Please Signup/Login to view")
    return redirect('dashboard')
  # print("I am in problems view")
  alltopic = topic.objects.all()
  top = topic.objects.filter(slug=slug).first()
  # if the slug is empty return 404
  if top is None:
    # messages.error(request,"Invalid Request !")
    return redirect('404')
  # if the topic is not active return 404
  if top.active is False:
    # messages.error(request,"This topic is currently not active")
    return redirect('404')
  prob = problem.objects.filter(topic=top).all().order_by('priority')
  total_problem = problem.objects.filter(topic=top).count()
  problem_solved = problem.objects.filter(topic=top,completed=request.user).count()
  problem_unsolved = total_problem - problem_solved
  userProbData = userProblemData.objects.filter(user = request.user).all()
  user = request.user
  # print(userProbData)
  # print(top)
  # print(prob)
  # print(userProbData)
  # print(problem_unsolved)
  context = {
    'alltopic':alltopic,
    'top':top,
    'prob':prob,
    'slug':slug,
    'userProbData':userProbData,
    'total_problem':total_problem,
    'problem_solved':problem_solved,
    'problem_unsolved':problem_unsolved,
    'user':user,

  }
  # messages.info(request,"Topic --> "+top.title)
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
    # messages.info(request,"A verification email has been send. Please verify your account")
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

# def sendEmail(request):
#   # I will send the email here
#   send_mail(
#     'Subject Test',
#     'Here is the test message.',
#     'support@quriosity.tech',
#     ['quriosity.tech@gmail.com'],
#     fail_silently=False,
#   )
#   return render(request,'email.html')

def forgotUsername(request):
  # return render(request,'forgot-username.html')
  return redirect('404')

def forgotPassword(request):
  # return render(request,'forgot-password.html')
  return redirect('404')

# trying the like functionality
# def like_button(request):
#   if request.method =="POST":
#     if request.POST.get("operation") == "like_submit" and request.is_ajax():
#       content_id=request.POST.get("content_id",None)
#       content=get_object_or_404(problem,pk=content_id)
#       if content.likes.filter(id=request.user.id): #already liked the content
#         content.likes.remove(request.user) #remove user from likes 
#         liked=False
#       else:
#         content.likes.add(request.user) 
#         liked=True
#       ctx={
#         # "likes_count":content.get_total_likes,
#         # "liked":liked,
#         "content_id":content_id
#       }
#       return HttpResponse(json.dumps(ctx), content_type='application/json')
#   contents=problem.objects.all()
#   already_liked=[]
#   id=request.user.id
#   for content in contents:
#     if(content.likes.filter(id=id).exists()):
#       already_liked.append(content.id)
#   ctx={"contents":contents,"already_liked":already_liked}
#   return render(request,"like/like_template.html",ctx)

def likePost(request):
  # print("i am here")
  #check if the user is anonymous then display the message to login
  if request.method == 'POST':
    user = request.user
    problem_id = request.POST.get('post_id')
    slug_id = request.POST.get('slug_id')
    problem_obj= problem.objects.get(id=problem_id)

    if user in problem_obj.liked.all():
      # user has already liked it before but is clicking the like button again
      problem_obj.liked.remove(user)
    else:
      problem_obj.liked.add(user)
    like_obj, created = like.objects.get_or_create(user=user,problem_id=problem_id).first()
    if not created:
      if like_obj.value == 'Like':
        like_obj.value = 'Unlike'
      else:
        like_obj.value = 'Like'
    like_obj.save()

  # return redirect(problems,slug_id)
  html = "<html><body>Hello World</body></html>"
  return HttpResponse(html)



def ProblemLike(request, pk):
  post = get_object_or_404(problem, id=request.POST.get('problem_id'))
  if post.liked.filter(id=request.user.id).exists():
    post.liked.remove(request.user)
  else:
    # print("i am here")
    post.liked.add(request.user)

  return redirect(request.META.get('HTTP_REFERER'))



def ProblemMark(request, pk):
  post = get_object_or_404(problem, id=request.POST.get('problem_id'))
  if post.completed.filter(id=request.user.id).exists():
    post.completed.remove(request.user)
  else:
    # print("i am here")
    post.completed.add(request.user)

  return redirect(request.META.get('HTTP_REFERER'))