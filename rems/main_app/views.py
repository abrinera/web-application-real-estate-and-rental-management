from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login 
from .models import Employee, Property, Transaction,Rental,Payment, Client
from .forms import EmployeeForm, ClientForm 
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
import uuid


# Create your views here.
def home(request):
    return render(request, 'home.html')
               
def signin(request):
    if request.method == "POST":
        username = request.POST['name']
        password = request.POST['password']
        
        user=authenticate(username=username, password=password)
        if user is not None:
            login(request,user) #login success
            request.session['username'] = username  # Store username in session
            return render(request,'dash_user.html') #User Dashboard e jabe
        
        else:
            messages.error(request,"Invalid Email or Password") 
            return redirect('signin')
    return render(request, 'signin.html')

def signup(request):
    if request.method == "POST":
        # Get form values
        username = request.POST['name']
        gender = request.POST['gender']
        email = request.POST['email']
        password = request.POST['password']
        
        if  User.objects.filter(username=username):
            messages.error(request,"This user already exists!")
            return redirect("signup")
        if  User.objects.filter(email=email):
            messages.error(request,"Username already exists!")
            return redirect("signup")
        if len(password)<6:
            messages.error(request,"Password is too short!")
            return redirect("signup")
                
        myuser = User.objects.create_user(username, email, password)
        myuser.Gender = gender
        
        myuser.save()
        messages.success(request,"Your account has been successfully created.")
        return redirect('signin') 
    return render(request, 'signup.html')

def ContactUs(request):
    return render(request, 'ContactUs.html')

def AboutUs(request):
    return render(request, 'AboutUs.html')

#user dashboard

def dash_user(request):    
    return render(request, 'dash_user.html')

def onebhk(request): 
    dont_view = ["Booked", "Sold"]
    exclude_filter = Q()
    for status in dont_view:
        exclude_filter |= Q(status=status) 
    prop_list=Property.objects.exclude(exclude_filter).filter(bed='1').values()
    return render(request, 'onebhk.html',{'prop_list':prop_list})
def twobhk(request): 
    dont_view = ["Booked", "Sold"]
    exclude_filter = Q()
    for status in dont_view:
        exclude_filter |= Q(status=status) 
    prop_list=Property.objects.exclude(exclude_filter).filter(bed='2').values()
    return render(request, 'onebhk.html',{'prop_list':prop_list})
def threebhk(request): 
    dont_view = ["Booked", "Sold"]
    exclude_filter = Q()
    for status in dont_view:
        exclude_filter |= Q(status=status) 
    prop_list=Property.objects.exclude(exclude_filter).filter(bed='3').values()
    return render(request, 'onebhk.html',{'prop_list':prop_list})
def fourbhk(request): 
    prop_list=Property.objects.filter(bed='4').values()
    return render(request, 'onebhk.html',{'prop_list':prop_list})
def fivebhk(request): 
    prop_list=Property.objects.filter(bed__gte='5').values() #underscor 2ta
    return render(request, 'onebhk.html',{'prop_list':prop_list})

def product_view_user(request):
    dont_view = ["Booked", "Sold"]
    # Create a filter to exclude the values in dont_view list
    exclude_filter = Q()
    for status in dont_view:
        exclude_filter |= Q(status=status)

    prop_list = Property.objects.exclude(exclude_filter).order_by('property_id')

    if request.method == "POST":
        prop_type = request.POST.get('type')
        location = request.POST.get('location')
        resident = request.POST.get('resident')
        bed = request.POST.get('bed')
        bath = request.POST.get('bath')
        area = request.POST.get('area')
        price = request.POST.get('price')
        
        # Build Q objects for each filter condition
        filters = Q()
        if location:
            filters &= Q(location__icontains=location)
        if resident:
            filters &= Q(resident__icontains=resident)
        if bed:
            filters &= Q(bed=bed)
        if bath:
            filters &= Q(bath=bath)
        if area:
            filters &= Q(area__lte=area)
        if price:
            filters &= Q(price__lte=price)
        
        if prop_type == 'Rent':
            prop_list = Rental.objects.filter(filters)
        else:
            prop_list = prop_list.filter(filters)  # Applying additional filters to the previous query
        
    return render(request, 'product_view_user.html', {'prop_list': prop_list})

def prop_detail(request):    
    property_id = request.GET.get('property_id')
    prop_id = Rental.objects.filter(rental_id=property_id)
    return render(request, 'prop_detail.html', {'prop_id': prop_id})    
        
def prop_detail_buy(request):    
    property_id = request.GET.get('property_id')
    prop_id = Property.objects.filter(property_id=property_id)
    return render(request, 'prop_detail_buy.html', {'prop_id': prop_id})
    
def booking_info(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client_instance = form.save(commit=False)
            # Assuming you have a way to retrieve the user instance associated with this client
            client_instance.username = request.user  # Set the username field
            client_instance.save()
            return redirect('booking_info')  # Redirect to a success page
    else:
        form = ClientForm()
    return render(request, 'booking_info.html', {'form': form})

def add_post(request):
    if request.method == 'POST':
        username = request.session.get('username', None)  # Retrieve username from session
        if username:
            location = request.POST['location']
            resident = request.POST['resident']
            contact_no = request.POST['contact_no']
            price = request.POST['price']
            area = request.POST['area']
            bed = request.POST['bedroom']
            bath = request.POST['bathroom']
            description = request.POST['description']
            image1 = request.FILES['image1']
            image2 = request.FILES['image2']
            
            unique_id = str(uuid.uuid4())[:8]  # Truncate to first 8 characters
            rental_id = f"{username}-{unique_id}"  # Concatenate username with unique identifier
            
            rental = Rental(
                rental_id=rental_id, location=location, resident=resident, contact_no=contact_no, 
                price=price, area=area, bed=bed, bath=bath, description=description, image1=image1, image2=image2
            )
            
            rental.save()
            return redirect('add_post')
        else:
            # Handle case where username is not found in session
            return HttpResponse("Please sign in first.")
    return render(request, 'add_post.html')

def my_ads_user(request):
    username = request.session.get('username', None)  # Retrieve username from session
    if username:
            rent_ads = Rental.objects.filter(rental_id__icontains= username)
            
    else:
            # Handle case where username is not found in session
            return HttpResponse("You haven't posted any ads yet.")
    return render(request, 'my_ads_user.html',{'rent_ads': rent_ads})

def pay(request):
    username = request.session.get('username')

    try:
        # Retrieve the user instance corresponding to the username
        user_instance = User.objects.get(username=username)
    except User.DoesNotExist:
        # Handle the case when the user does not exist
        return HttpResponse("User matching query does not exist.")

    # Retrieve all client instances associated with the user
    client_instances = Client.objects.filter(username=user_instance)

    # Handle the case when no client instance is found
    if not client_instances.exists():
        return HttpResponse("No client associated with the user.")

    # Retrieve all transactions associated with the client instances
    trans = Transaction.objects.filter(client_nid__in=client_instances.values_list('nid', flat=True))

    # Render the pay.html template with the transactions information
    return render(request, 'pay.html', {'trans': trans})
    
def my_info(request):
    return render(request,'my_info')    




def dash_employee(request):
    return render(request, 'dash_employee.html')

def add_property(request):
    if request.method=="POST" and request.FILES['image1']:
        property_id = request.POST['property_id']
        location = request.POST['location']
        resident = request.POST['resident']
        status = request.POST['status']
        area = request.POST['area']
        price = request.POST['price']
        bed = request.POST['bed']
        bath = request.POST['bath']
        description = request.POST['description']
        
        image1 = request.FILES['image1']
        fs = FileSystemStorage()
        img1 = fs.save(image1.name, image1)
        img1_url = fs.url(img1)
        
        image2 = request.FILES['image2']
        fs = FileSystemStorage()
        img2 = fs.save(image2.name, image2)
        img2_url = fs.url(img2)
        
 
        new_prop =  Property(property_id=property_id, location=location, resident=resident,  status=status, price=price,
                             bed=bed, bath=bath, description=description, area=area,image1=img1_url, image2=img2_url)
        new_prop.save()
        messages.success(request,"New Property  added Successfully")
        return redirect('add_property')
    
    return render(request, 'add_property.html')

def add_rental(request):
    if request.method == 'POST' and request.FILES['image1']:
        rental_id = request.POST['r_id']
        location = request.POST['location']
        resident = request.POST['resident']
        contact_no = request.POST['contact_no']
        price = request.POST['price']
        area= request.POST['area']
        bed = request.POST['bed']
        bath = request.POST['bath']
        description = request.POST['description']
        
        image1 = request.FILES['image1']
        fs = FileSystemStorage()
        img1 = fs.save(image1.name, image1)
        img1_url = fs.url(img1)
        
        image2 = request.FILES['image2']
        fs = FileSystemStorage()
        img2 = fs.save(image2.name, image2)
        img2_url = fs.url(img2)

        rental_new = Rental(rental_id=rental_id, location=location,resident=resident,contact_no=contact_no,
                        price=price,area=area, bed=bed, bath=bath, description=description,
                        image1=img1_url, image2=img2_url)
        rental_new.save()
        messages.success(request,"New Rental Property added Successfully")
        return redirect('add_rental')
    
    return render(request, 'add_rental.html')

def transaction(request):
    trans_list=Transaction.objects.all().order_by('entry_date').reverse() #view query
    if request.method=="POST":
        trans_no = request.POST['trans_no']
        property_id = request.POST["property_id"]
        client_nid =  request.POST['client_nid']   
        fname= request.POST['fname']
        lname= request.POST['lname']
        account_no= request.POST['account_no']
        amount = int(request.POST['amount'])
        payment_method= request.POST['payment_method']
        
     # Retrieve the Property instance corresponding to the property_id
        property_instance = Property.objects.get(property_id=property_id)

        new_trans = Transaction(trans_no=trans_no, pid=property_instance, client_nid=client_nid, fname=fname, lname=lname,
                                account_no=account_no, amount=amount, payment_method=payment_method)
        
        # Check if a Payment object with the given property_id exists
        try:
            payment_instance = Payment.objects.get(pid=property_instance)
            # If it exists, update only some values
            payment_instance.recent_trans=trans_no
            payment_instance.total_paid += amount
            payment_instance.due=payment_instance.price - payment_instance.total_paid
            if payment_instance.due==0:
                payment_instance.payment_status="Payment Complete"
            else:
                payment_instance.payment_status="Ongoing Payment"
            payment_instance.save()
        except Payment.DoesNotExist:
            due=property_instance.price-amount
            if due==0:
                payment_status="Payment Complete"
                update_status= Property.objects.get(property_id=property_id)
                update_status.status="Sold"
                update_status.save()
            elif due<0:
                return HttpResponse("Payment Amount is invalid")    
            else:
                payment_status="Ongoing Payment"
            # If it doesn't exist, add a new Payment object with all the values
            payment_instance = Payment(pid=property_instance, client_nid=client_nid, price=property_instance.price,
                                        total_paid=amount,due=due, payment_status=payment_status,recent_trans=trans_no)
            
            payment_instance.save()
            
            update_status= Property.objects.get(property_id=property_id)
            update_status.status="Booked"
            update_status.save()

        new_trans.save()
        messages.success(request,"New Transaction has been added Successfully")
        
        return redirect('transaction')
    return render(request, 'transaction.html',
                  {'trans_list': trans_list})

def view_property_rent(request):
    prop_list=Rental.objects.all().order_by('entry_date')
    return render (request,'view_property.html', {"prop_list": prop_list})

def view_property(request):
    dont_view = ["Booked", "Sold"]
    exclude_filter = Q()
    for status in dont_view:
        exclude_filter |= Q(status=status)
    prop_list = Property.objects.exclude(exclude_filter).order_by('property_id')    

    if request.method == 'POST':
        query = request.POST['searched']
        if query:
            prop_list = Property.objects.exclude(exclude_filter).filter(Q(property_id__icontains=query) | Q(location__icontains=query))
    return render(request, 'view_property.html', {"prop_list": prop_list})

def client_booking(request):
    view="Booked"
    prop_list = Property.objects.filter(status=view)
    return render(request, 'client_booking.html', {"prop_list": prop_list})

def client_info(request):
    clients = Client.objects.all()  # Retrieve all client objects from the database
    return render(request, 'client_info.html', {'clients': clients})

def payment_info(request):
    pay_list=Payment.objects.all()
    return render(request, 'payment_info.html',{"pay_list":pay_list})

def view_employee(request):
    emp_list=Employee.objects.all().order_by('employee_id')
    return render(request, 'view_employee.html',{'emp_list':emp_list})

def update_property(request): 
    return render(request, 'update_property.html')        

def update_rental(request):
    return render(request, 'update_rental.html')

def employee_signinup(request): #nd
        if request.method == "POST":
            username = request.POST['username']
            employee_id = request.POST['employee_id']
            password = request.POST['password']
            
            return render(request,'dash_employee.html')

        return render(request, 'employee_signinup.html')
    
def employee_signup(request): #ND
        if request.method == "POST":
            form = EmployeeForm(request.POST or None)
            if form.is_valid():
                if  Employee.objects.filter(employee_id=Employee.employee_id):
                    form.save()
                else:
                 messages.error(request,"Invalid Email or Employee ID")
                return redirect('employee_signinup')
            return redirect('employee_signinup') 
