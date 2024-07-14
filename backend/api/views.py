

from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout as auth_logout
from django.contrib.auth.models import User  
from django.http import HttpResponse,JsonResponse
from .models import Vendor,Customer


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if user exists with the given email
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None

        if user is not None:
            # Authenticate user using email and password
            user = authenticate(request, username=user.username, password=password)

            if user is not None and user.is_active:
                
                
                return redirect('dashboard')  
            else:
                # Authentication failed or user is not active
                error = 'Invalid credentials or user is not active.'
                return render(request, 'login.html', {'error': error})

        else:
            # No user found with the given email
            error = 'No user found with this email.'
            return render(request, 'login.html', {'error': error})

    return render(request, 'login.html')

def logout(request): #Logout Done 
    auth_logout(request)
    
    return redirect('login')


def dashboard(request):
    return render(request,'dashboard.html')


def addVendor(request):  #Basic Serup of add vendor done 
    if request.method == 'POST':
        vendor_name = request.POST.get('vendorName')
        vendor_address = request.POST.get('vendorAddress')
        vendor_gst_number = request.POST.get('vendorGstNumber')
        vendor_phone_number = request.POST.get('vendorPhoneNumber')
        
        ''' Checking of the valid data '''
        if not vendor_name or not vendor_address or not vendor_gst_number or not vendor_phone_number: 
            
            return JsonResponse({'success': False, 'message': 'All fields are required.'}, status=400)
        
        try:
            
            Vendor.objects.create(
                vendorName=vendor_name,
                vendorAddress=vendor_address,
                vendorGstNumber=vendor_gst_number,
                vendorPhoneNumber=vendor_phone_number
            )
            
            
            return JsonResponse({'success': True, 'message': 'Vendor added successfully.'})
        except Exception as e:
            
            return JsonResponse({'success': False, 'message': str(e)}, status=500)
    
    
    return render(request, 'addVendor.html')


def addCustomer(request):
    if request.method == 'POST':
        customer_first_name = request.POST.get('customerFirstName')
        customer_middle_name = request.POST.get('customerMiddleName')
        customer_last_name = request.POST.get('customerLastName')
        customer_address = request.POST.get('customerAddress')
        customer_phone_number = request.POST.get('customerPhoneNumber')
        
        
        if not customer_first_name or not customer_last_name or not customer_address or not customer_phone_number:
            
            return JsonResponse({'success': False, 'message': 'All fields are required.'}, status=400)
        
        try:
            
            Customer.objects.create(
                customerFirstName=customer_first_name,
                customerMiddleName=customer_middle_name,
                customerLastName=customer_last_name,
                customerAddress=customer_address,
                customerPhoneNumber=customer_phone_number
            )
            
            
            return JsonResponse({'success': True, 'message': 'Customer added successfully.'})
        except Exception as e:
            
            return JsonResponse({'success': False, 'message': str(e)}, status=500)
    
    
    return render(request, 'addCustomer.html')
    