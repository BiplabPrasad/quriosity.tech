from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('base_copy/',views.base_copy,name="base_copy"),
    path('base/',views.base,name="base"),
    path('signup/',views.signup,name="signup"),
    path('login/',views.login,name="login"),
    path('activity/',views.activity,name="activity"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('faq/',views.faq,name="faq"),
    path('profile/',views.profile,name="profile"),
    path('settings/',views.settings,name="settings"),
    path('problems/',views.problems,name="problems"),
    path('logout/',views.logout,name="logout"),
    # for signup
    path('signup/handleSignup/',views.handleSignup,name="handleSignup"),
]