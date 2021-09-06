from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('base_copy/',views.base_copy,name="base_copy"),
    path('base/',views.base,name="base"),
    path('signup/',views.signup,name="signup"),
    path('login/',views.login,name="login")
]