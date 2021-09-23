from django.urls import  path 
from .views import HomePage 
from .views import SignupView



urlpatterns = [
    path('',HomePage.as_view(),name='home'),
    path('signup/',SignupView.as_view(),name='signup'),
]