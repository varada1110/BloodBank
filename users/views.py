from django.http.response import JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import BloodBank

# Create your views here.
def form(request):

    if 'username' in request.session:
        if request.method =='POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            number = request.POST.get('number')
            bloodGroup = request.POST.get('bloodGroup')
            
            BloodObj=BloodBank(name=name,email=email,number=number,bloodGroup=bloodGroup)
            BloodObj.save()
            return redirect('display')
        else:
            return render(request,'form.html')
    else:
        return redirect('/')

        
def display(request):
    if 'username' in request.session:
        blood = BloodBank.objects.all()
        return render(request,'display.html',{'blood':blood})
    return redirect('/')   