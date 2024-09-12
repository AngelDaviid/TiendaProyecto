from django.urls import path
from . import views

urlpatterns =[
    path('', views.Home, name='Home'),
    path('services/', views.services),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.signout, name='logout'),
]