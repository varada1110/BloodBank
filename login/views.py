
from django.http.response import JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

# Create your views here.



def main(request):
    
    if request.method == 'POST':
        username =  request.POST['name']
        email = request.POST['email']
        password = request.POST['pwd']
        
        if User.objects.filter(email=email).exists():
            return render(request,'signup.html',{'error':"Email already taken"}) 
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save();
            print("user created")
            return render(request,'login.html')
    else:
        return render(request,'signup.html') 
       



def login_user(request):

    if 'username' in request.session:
        return render(request,'display.html')
    if request.method == 'POST': 
        username = request.POST.get('username')
        password = request.POST.get('password') 

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            request.session['username'] = username
            return JsonResponse(
                {'success':True},
                safe=False
            )

        else:
            return JsonResponse(
                {'success':False},
                safe=False
            )
    else:
        return render(request,'login.html')

   

def logout_user(request):
    if 'username' in request.session:
        request.session.flush()
    return redirect('/')



