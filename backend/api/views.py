

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


# def vpo(request):
#     if request.method == 'POST':
#         # Retrieve form data from POST request
#         vendor_id = request.POST.get('vendor')
#         serial_num = request.POST.get('serial_num')
#         product_id = request.POST.get('product')
#         UOM = request.POST.get('UOM')
#         QTY = request.POST.get('QTY')
#         rate = request.POST.get('Rate')
#         total = request.POST.get('total')
#         discount = request.POST.get('discount')
#         transportation = request.POST.get('transportation')
#         total_taxable_amount = request.POST.get('total_taxable_amount')
#         gst = request.POST.get('gst')
#         total_amount = request.POST.get('total_amount')
#         proforma_invoice = request.FILES.get('proforma_invoice') if 'proforma_invoice' in request.FILES else None
        
#         # Retrieve vendor and product objects from their models
#         vendor = Vendor.objects.get(vendor_id=vendor_id)
#         product = Product.objects.get(product_id=product_id)

#         # Create and save VPO object
#         vpo = VPO(
#             vendor=vendor,
#             serial_num=serial_num,
#             product=product,
#             UOM=UOM,
#             QTY=QTY,
#             rate=rate,
#             total=total,
#             discount=discount,
#             transportation=transportation,
#             total_taxable_amount=total_taxable_amount,
#             gst=gst,
#             total_amount=total_amount,
#             proforma_invoice=proforma_invoice
#         )
#         vpo.save()

#         return HttpResponse('VPO created successfully!')  # Or redirect to a success page
#     else:
#         # Fetch all vendors and products for the initial form load
#         vendors = Vendor.objects.all()
#         products = Product.objects.all()
#         context = {'vendors': vendors, 'products': products}
#         return render(request, 'vpo.html', context)
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_GET
from .models import Product

@require_GET
def get_product_price(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    data = {
        'price': product.price,
    }
    return JsonResponse(data)













    
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle


from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from datetime import datetime

def generate_vpo_pdf(buffer, vendor, serial_nums, product_ids, UOMs, qtys, rates, totals, discount, transportation, total_taxable_amount, gst, total_amount, delivery_address, delivery_city, delivery_state, delivery_contact, bank_name, account_number, bank_ifsc,invoice_number):
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    margin = inch

    today_date = datetime.now().strftime("%d-%b-%Y")
    c.setFont("Helvetica", 10)
    c.drawRightString(width - margin, height - margin, f"Invoice Number: {invoice_number}")
    c.drawRightString(width - margin, height - margin - 15, f"Date: {today_date}")

    # Heading
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width / 2, height - margin, "Proforma Invoice")

    # Gap between heading and company details
    gap_height = -0.6 * inch  # Adjusted gap height

    # Company details table
    company_details = [
        ["Seller"],
        [vendor.vendorName],
        [vendor.vendorAddress],
        [vendor.vendorPhoneNumber],
        [vendor.vendorGstNumber],
    ]
    company_table = Table(company_details, colWidths=[width - 2 * margin])
    company_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('FONTSIZE', (0, 0), (-1, -1), 10.),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    company_table_width, company_table_height = company_table.wrap(width - 2 * margin, height)
    y = height - 2 * margin - gap_height - company_table_height
    company_table.drawOn(c, margin, y)

    line_y = y - 1  # Adjust position of the line if necessary
    c.setStrokeColor(colors.black)
    c.setLineWidth(1)
    c.line(margin, line_y, width - margin, line_y)
    c.line(margin, line_y + 3, width - margin, line_y + 3)

    # Buyer details table
    buyer_details = [
        ["Buyer"],
        ["Sarla Agencies"],
        ["36,Rikhi Bhuvan,L.N. Road,Matunga East Mumbai,Mumbai Suburban Maharashtra, 400019"],
        ["Phone: (987) 654-3210"]
    ]
    buyer_table = Table(buyer_details, colWidths=[width - 2 * margin])
    buyer_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    buyer_table_width, buyer_table_height = buyer_table.wrap(width - 2 * margin, height)
    y -= company_table_height + 20  # Adjust y-coordinate to fit the new section
    buyer_table.drawOn(c, margin, y)

    # Gap before table header
    y -= 0.5 * inch

    # Table data
    table_data = [["Sr No.", "Description", "UOM", "QTY", "Rate", "Total"]]
    for i in range(len(serial_nums)):
        product = Product.objects.get(product_id=product_ids[i])
        row = [
            serial_nums[i],
            product.description,
            UOMs[i],
            str(qtys[i]),
            str(rates[i]),
            str(totals[i])
        ]
        table_data.append(row)

    # Table style
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])

    # Create table
    product_table = Table(table_data, colWidths=[50, 160, 60, 60, 70, 67])
    product_table.setStyle(table_style)
    product_table_width, product_table_height = product_table.wrap(width - 2 * margin, height)
    y -= product_table_height

    # Draw the product table
    product_table.drawOn(c, margin, y)

    # Move y-coordinate down for summary table
    y -= -0.2 * inch  # Adjust this if you need more space between the product table and summary table

    # Summary table
    summary_data = [
        ["Discount", discount],
        ["Transportation", transportation],
        ["Total Taxable Amount", total_taxable_amount],
        ["GST", gst],
        ["Total Amount", total_amount]
    ]
    summary_table = Table(summary_data, colWidths=[400, 67])
    summary_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'RIGHT'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    summary_table_width, summary_table_height = summary_table.wrap(width - 2 * margin, height)
    y -= summary_table_height + 15  # Adjust margin if necessary
    summary_table.drawOn(c, margin, y)

    notes_title = "Notes:"
    notes_content = f"This is Proforma only, Tax invoice will be issued upon actual purchase.<br/>Payment Terms: 100% advance with confirm PO.<br/><br/>Delivery Address: {delivery_address}<br/>{delivery_city}<br/>{delivery_state}<br/>{delivery_contact}."
    styles = getSampleStyleSheet()
    notes_style = ParagraphStyle(name='NotesStyle', fontSize=10, leading=12)
    notes_paragraph = Paragraph(f'<b>{notes_title}</b><br/>{notes_content}', style=notes_style)

    notes_width, notes_height = notes_paragraph.wrap(width - 2 * margin, height)
    y -= notes_height + 0.5 * inch  # Adjust y-coordinate to fit notes section
    notes_paragraph.drawOn(c, margin, y)

    # Stamp and Signature section
    # Create a style for the stamp and signature section
    stamp_signature_style = ParagraphStyle(name='StampSignatureStyle', fontSize=10, leading=12)

    # Define content
    stamp_signature_content = [
        ["Authorized Signature: ____________________", "Stamp: ____________________"],
        ["",vendor.vendorName]
    ]

    # Create Table for Stamp and Signature
    stamp_signature_table = Table(stamp_signature_content, colWidths=[width / 2 - margin, width / 2 - margin])
    stamp_signature_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('TOPPADDING', (0, 0), (-1, -1), 12),
    ]))

    # Draw the stamp and signature table
    stamp_signature_width, stamp_signature_height = stamp_signature_table.wrap(width - 2 * margin, height)
    y -= stamp_signature_height + 0.5 * inch  # Adjust y-coordinate to fit stamp and signature section
    stamp_signature_table.drawOn(c, margin, y)

    # Draw a box around the entire content
    content_top = height - 1.3 * inch
    content_bottom = margin - .1 * inch
    content_left = margin + -0.2 * inch  # Increased left margin
    content_right = width - margin - -0.2 * inch  # Increased right margin

    c.setStrokeColor(colors.black)
    c.setLineWidth(1)
    c.rect(content_left, content_bottom, content_right - content_left, content_top - content_bottom)

    # Finalize the PDF
    c.showPage()
    c.save()




from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.base import ContentFile
from io import BytesIO
from .models import Vendor, Product, VPO
from django.utils import timezone
import random
import string

def generate_invoice_number(vendor):
    try:
        # Retrieve the first 4 letters of the vendor name (in uppercase)
        company_prefix = vendor.vendorName[:4].upper()

        # Get the current month and year
        now = timezone.now()
        month = now.strftime('%m')
        year = now.strftime('%y')

        # Get the latest invoice number for this vendor
        last_invoice = VPO.objects.filter(vendor=vendor).order_by('-id').first()
        if last_invoice and last_invoice.invoice_number:
            # Extract the numeric part of the last invoice number
            last_number_str = last_invoice.invoice_number[-3:]
            try:
                last_number = int(last_number_str)
            except ValueError:
                last_number = 0
        else:
            last_number = 0

        # Generate the next sequential number
        next_number = str(last_number + 1).zfill(3)

        # Format the invoice number
        invoice_number = f"{company_prefix}{month}{year}{next_number}"
        return invoice_number
    except Exception as e:
        print(f"Error generating invoice number: {e}")
        return None  # or handle as appropriate


def vpo(request):
    if request.method == 'POST':
        vendor_id = request.POST.get('vendor')
        serial_nums = request.POST.getlist('serial_num')
        product_ids = request.POST.getlist('product')
        UOMs = request.POST.getlist('UOM')
        qtys = request.POST.getlist('QTY')
        rates = request.POST.getlist('Rate')
        totals = request.POST.getlist('total')
        discount = float(request.POST.get('discount', 0))  # Use float for decimal values
        transportation = float(request.POST.get('transportation', 0))  # Use float for decimal values
        total_taxable_amount = float(request.POST.get('total_taxable_amount', 0))  # Use float for decimal values
        gst = float(request.POST.get('gst', 0))  # Use float for decimal values
        total_amount = float(request.POST.get('total_amount', 0)) 
        delivery_address = request.POST.get('delivery_address')
        delivery_city = request.POST.get('delivery_city')
        delivery_state = request.POST.get('delivery_state')
        delivery_contact = request.POST.get('delivery_contact')
        bank_name = request.POST.get('bank_name')
        account_number = request.POST.get('account_number')
        bank_ifsc = request.POST.get('bank_ifsc')

        # Retrieve vendor
        vendor = Vendor.objects.get(vendor_id=vendor_id)

        # Generate invoice number
        invoice_number = generate_invoice_number(vendor)

        # Create VPO objects
        vpo_ids = []
        for i in range(len(serial_nums)):
            product = Product.objects.get(product_id=product_ids[i])
            vpo = VPO(
                vendor=vendor,
                serial_num=serial_nums[i],
                product=product,
                uom=UOMs[i],
                qty=qtys[i],
                rate=rates[i],
                total=totals[i],
                discount=discount,
                transportation=transportation,
                total_taxable_amount=total_taxable_amount,
                gst=gst,
                total_amount=total_amount,
                delivery_address=delivery_address,
                delivery_city=delivery_city,
                delivery_state=delivery_state,
                delivery_contact=delivery_contact,
                bank_name=bank_name,
                account_number=account_number,
                bank_ifsc=bank_ifsc,
                invoice_number=invoice_number,
                # Add more fields as needed
            )
            vpo.save()
            vpo_ids.append(vpo.id)

        # Retrieve the last created VPO to get the generated invoice number
        vpo = VPO.objects.get(id=vpo_ids[-1])

        # Generate PDF
        buffer = BytesIO()
        generate_vpo_pdf(
            buffer, vendor, serial_nums, product_ids, UOMs, qtys, rates, totals, 
            discount, transportation, total_taxable_amount, gst, total_amount,
            delivery_address, delivery_city, delivery_state, delivery_contact,
            bank_name, account_number, bank_ifsc, invoice_number
            # Add more fields as needed
        )
        pdf = buffer.getvalue()
        buffer.close()

        # Save PDF to the database
        vpo.proforma_invoice.save(f'vpo_{vpo.invoice_number}.pdf', ContentFile(pdf))

        # Create response for download
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="vpo_{vpo.invoice_number}.pdf"'
        return response

    else:
        vendors = Vendor.objects.all()
        products = Product.objects.all()
        context = {'vendors': vendors, 'products': products}
        return render(request, 'vpo.html', context)

def viewvpo(request):
    return render(request,'viewvpo.html')