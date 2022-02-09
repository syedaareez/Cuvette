from django.urls import path
from .views import indexPage,loginUser,logoutUser,Dashboard

app_name='basic_app'

urlpatterns = [
    path('index/',indexPage),
    path('login/',loginUser,name='login'),
    path('logout/',logoutUser,name='logout'),
    path('dashboard/',Dashboard,name='dashboard'),
    
]
