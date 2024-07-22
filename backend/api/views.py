

from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout as auth_logout
from django.contrib.auth.models import User  
from django.http import HttpResponse,JsonResponse
from .models import Vendor,Customer,Company,Product,VPO



def landingpage(request):
    return render(request, 'landingpage.html') 

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
        vendor_id = request.POST.get('vendor_id')
        vendor_name = request.POST.get('vendorName')
        vendor_address = request.POST.get('vendorAddress')
        vendor_gst_number = request.POST.get('vendorGstNumber')
        vendor_phone_number = request.POST.get('vendorPhoneNumber')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')

        # Checking of the valid data
        if not vendor_id or not vendor_name or not vendor_address or not vendor_gst_number or not vendor_phone_number or not city or not state or not pincode:
            messages.error(request, 'All fields are required.')
            return redirect('addVendor')
        
        try:
            Vendor.objects.create(
                vendor_id = vendor_id,
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

from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Product

def addProduct(request):
    if request.method == 'POST':
        product_id = request.POST.get('productId')
        product_type = request.POST.get('productType')
        description = request.POST.get('description')
        count = request.POST.get('count')
        price = request.POST.get('price')
        vase_type = request.POST.get('vaseType')
        vase_count = request.POST.get('vaseCountInput')

        # Create a new Product object and save to database
        product = Product(
            product_id=product_id,
            product_type=product_type,
            description=description,
            count=count,
            price=price,
            vase_type=vase_type,
            vase_count=vase_count
        )
        product.save()

        # Redirect to a success page or wherever you want
        return redirect('addProduct')  # Replace 'success_page' with your actual URL name

    # Render the form initially or on GET request
    return render(request, 'addProduct.html')


def vpo(request):
    if request.method == 'POST':
        # Retrieve form data from POST request
        vendor_id = request.POST.get('vendor')
        serial_num = request.POST.get('serial_num')
        product_id = request.POST.get('product')
        UOM = request.POST.get('UOM')
        QTY = request.POST.get('QTY')
        rate = request.POST.get('Rate')
        total = request.POST.get('total')
        discount = request.POST.get('discount')
        transportation = request.POST.get('transportation')
        total_taxable_amount = request.POST.get('total_taxable_amount')
        gst = request.POST.get('gst')
        total_amount = request.POST.get('total_amount')
        proforma_invoice = request.FILES.get('proforma_invoice') if 'proforma_invoice' in request.FILES else None
        
        # Retrieve vendor and product objects from their models
        vendor = Vendor.objects.get(vendor_id=vendor_id)
        product = Product.objects.get(product_id=product_id)

        # Create and save VPO object
        vpo = VPO(
            vendor=vendor,
            serial_num=serial_num,
            product=product,
            UOM=UOM,
            QTY=QTY,
            rate=rate,
            total=total,
            discount=discount,
            transportation=transportation,
            total_taxable_amount=total_taxable_amount,
            gst=gst,
            total_amount=total_amount,
            proforma_invoice=proforma_invoice
        )
        vpo.save()

        return HttpResponse('VPO created successfully!')  # Or redirect to a success page
    else:
        # Fetch all vendors and products for the initial form load
        vendors = Vendor.objects.all()
        products = Product.objects.all()
        context = {'vendors': vendors, 'products': products}
        return render(request, 'vpo.html', context)


