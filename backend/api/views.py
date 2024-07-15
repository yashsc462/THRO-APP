

from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout as auth_logout
from django.contrib.auth.models import User  
from django.http import HttpResponse,JsonResponse
from .models import Vendor,Customer,Company,Product


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


from django.contrib import messages

def addVendor(request):
    if request.method == 'POST':
        vendor_name = request.POST.get('vendorName')
        vendor_address = request.POST.get('vendorAddress')
        vendor_gst_number = request.POST.get('vendorGstNumber')
        vendor_phone_number = request.POST.get('vendorPhoneNumber')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')

        # Checking of the valid data
        if not vendor_name or not vendor_address or not vendor_gst_number or not vendor_phone_number or not city or not state or not pincode:
            messages.error(request, 'All fields are required.')
            return redirect('addVendor')
        
        try:
            Vendor.objects.create(
                vendorName=vendor_name,
                vendorAddress=vendor_address,
                vendorGstNumber=vendor_gst_number,
                vendorPhoneNumber=vendor_phone_number,
                city=city,
                state=state,
                pincode=pincode
            )
            messages.success(request, 'Vendor added successfully.')
            return redirect('addVendor')
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
            return redirect('addVendor')

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
    



def addCompany(request):
    if request.method == 'POST':
        company_name = request.POST.get('companyName')
        company_address = request.POST.get('companyAddress')
        company_gst_number = request.POST.get('companyGstNumber')
        company_phone_number = request.POST.get('companyPhoneNumber')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')

        # Checking of the valid data
        if not company_name or not company_address or not company_gst_number or not company_phone_number or not city or not state or not pincode:
            messages.error(request, 'All fields are required.')
            return redirect('addCompany')
        
        try:
            Company.objects.create(
                companyName=company_name,
                companyAddress=company_address,
                companyGstNumber=company_gst_number,
                companyPhoneNumber=company_phone_number,
                city=city,
                state=state,
                pincode=pincode
            )
            messages.success(request, 'Company added successfully.')
            return redirect('addCompany')
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
            return redirect('addCompany')

    return render(request, 'addCompany.html')




def vendorList(request):
    vendors = Vendor.objects.all()
    return render(request, 'vendorList.html', {'vendors': vendors})

def addProduct(request):
    if request.method == 'POST':
        # Extract form data from POST request
        productId = request.POST.get('productId')
        productImage = request.FILES.get('productImage')
        productFirstName = request.POST.get('productFirstName')
        productDescription = request.POST.get('productDescription')
        productvalue = request.POST.get('productvalue')
        productattribute = request.POST.get('productattribute')
        productChoose = request.POST.get('productChoose')
        productChoose1 = request.POST.get('productChoose1')
        productNumber = request.POST.get('productNumber')
        productNumber1 = request.POST.get('productNumber1')

        # Create new Product instance
        try:
            Product.objects.create(
                productId = productId,
                productImage=productImage,
                productFirstName=productFirstName,
                productDescription=productDescription,
                productvalue=productvalue,
                productattribute=productattribute,
                productChoose=productChoose,
                productChoose1=productChoose1,
                productNumber=productNumber,
                productNumber1=productNumber1
            )
        
            # Redirect to a success page or back to the addProduct page
            return redirect('addProduct')  # Redirects to the same page after form submission

        except Exception as e:
            # Handle any exceptions, such as validation errors or database errors
            # You can add error handling logic here or log the exception
            print(f"Error saving product: {e}")
            # Optionally, you can render an error message to the user
            return render(request, 'addProduct.html', {'error_message': 'Failed to add product. Please try again.'})

    else:
        # If request method is not POST, render the form page
        return render(request, 'addProduct.html')





