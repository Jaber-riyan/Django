from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='homepage'),
    path('signup/',views.signup, name='signuppage'),
    path('login/',views.loginform, name='loginpage'),
    path('logout/',views.user_logout, name='logoutpage'),
    path('profile/',views.profile, name='profilepage'),
    path('passchange/',views.pass_change, name='passchange'),
    path('passchange2/',views.pass_change2, name='passchange2'),
]
