from django.shortcuts import render, redirect

# Create your views here.


def Login(request):
    if request.method=="POST":
        #if request.Post.get('UserName') == "admin" and request.Post.get('Password') == "admin":
            return render(request, 'hmc.html')
        #else:
            #return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def HMC(request):
    return render(request, 'hmc.html')

