from django.urls import path

from . import views

urlpatterns = [
    path('display',views.display,name='display'),
    path('form',views.form,name='form')

]