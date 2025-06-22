from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index,name='index'),
    
    #Logout User
    path('logout-user/',views.logout_user, name='logout_user'),
    
    #Login User
    path('login-user/',views.login_user, name='login_user'),
    
    
]