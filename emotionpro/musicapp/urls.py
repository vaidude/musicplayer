from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('index/',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('home/',views.home,name='home'),
    
    path('adlogin/', views.adlogin, name='adlogin'),
    path('adhome/', views.adhome, name='adhome'),
    path('userlist/', views.userlist, name='userlist'),
    path('deleteuser/<int:id>/', views.deleteuser, name='deleteuser'),
    
    path('detect_emotion/',views.detect_emotion,name='detect_emotion'),
    path('profile/', views.profile, name='profile'),
    path('editprofile/', views.editprofile, name='editprofile'),
]
