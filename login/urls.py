from django.urls import path
from . import views
urlpatterns = [

    path('',views.login_user,name='login_user'),
    path('main', views.main, name='main'),
    path('logout_user', views.logout_user, name='logout_user'),
    
    

    
]