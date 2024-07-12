from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Authenticate user
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            # User authenticated successfully, log in
            login(request, user)
            return redirect('dashboard')  # Replace 'dashboard' with your desired redirect URL after login
        else:
            # Authentication failed
            return render(request, 'login.html', {'error': 'Invalid email or password'})
    
    return render(request, 'login.html')


def dashboard(request):
    return render(request,'dashboard.html')