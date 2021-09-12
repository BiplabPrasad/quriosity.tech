from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('base_copy/',views.base_copy,name="base_copy"),
    path('base/',views.base,name="base"),
    path('signup/',views.signup,name="signup"),
    path('log_in/',views.log_in,name="log_in"),
    path('activity/',views.activity,name="activity"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('faq/',views.faq,name="faq"),
    path('profile/',views.profile,name="profile"),
    path('settings/',views.settings,name="settings"),
    path('search/',views.search,name="search"),
    path('404/',views.page404,name="404"),
    path('email/',views.sendEmail,name="email"),
    path('problems/<str:slug>',views.problems,name="problems"),
    # for handling logout
    path('log_out/',views.log_out,name="log_out"),
    # for handling signup
    path('signup/handleSignup/',views.handleSignup,name="handleSignup"),
    # for handling Login
    path('log_in/handleLogin/',views.handleLogin,name="handleLogin"),
]