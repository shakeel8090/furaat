from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
 
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():  # Corrected 'object' to 'objects'
                messages.info(request, 'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():  # Corrected 'object' to 'objects'
                messages.info(request, 'Email taken')
                return redirect('register')
            else:
                new_user = User.objects.create_user(username=username, password=password1, email=email, last_name=last_name, first_name=first_name)
                new_user.save()
                print('User created')
            return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            # Handle the case where passwords do not match
            # You can add appropriate error handling here

    return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


          
    

    


    
