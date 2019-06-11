from django.urls import path
from profileApp import views

#TEMPLATE URL!

app_name = 'profileApp'

urlpatterns = [
    path('register',views.register,name='register'),
]