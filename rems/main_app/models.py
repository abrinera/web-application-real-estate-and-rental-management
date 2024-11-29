from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    phone = models.IntegerField()
    age = models.IntegerField()
    employee_id= models.CharField(max_length=6, primary_key=True, unique=True)
    username= models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=10) #Male/Female
    position= models.CharField(max_length=50)
    branch= models.CharField(max_length=50)
    password= models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return " EMPID:"+ self.employee_id+ '  Name:' + self.first_name +" "+ self.last_name +"  Position:"+ self.position

class Property(models.Model):
    property_id = models.CharField(max_length=10, primary_key=True,unique=True)
    location = models.CharField(max_length=50) 
    resident = models.CharField(max_length=50)  
    status = models.CharField(max_length=50)
    price =  models.PositiveIntegerField()
    area = models.IntegerField()
    bed = models.IntegerField()
    bath = models.IntegerField()
    description =  models.TextField()
    image1 = models.ImageField(null=True, blank= True, upload_to='website_img/')
    image2 = models.ImageField(null=True, blank= True, upload_to='website_img/')
    
    entry_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return "ID:"+ self.property_id  + "   Status:" + self.status+ "    Location:" + self.location
        
class Rental(models.Model):
    rental_id = models.CharField(max_length=20, unique=True, primary_key=True)   
    location = models.CharField(max_length=50) 
    resident = models.CharField(max_length=50)  
    contact_no = models.CharField(max_length=15)
    price =  models.DecimalField(max_digits=100, decimal_places=2)
    area = models.IntegerField()
    bed = models.IntegerField()
    bath = models.IntegerField()
    description =  models.TextField()
    image1 = models.ImageField(null=True, blank= True, upload_to='website_img/')
    image2 = models.ImageField(null=True, blank= True, upload_to='website_img/')
    
    entry_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return "  ID:" + self.rental_id+ "  ----->  "+"   Location:" + self.location

class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    phone = models.IntegerField()
    age = models.IntegerField()
    nid= models.CharField(max_length=10, primary_key=True, unique=True)
    address= models.CharField(max_length=200, blank=True)
    gender = models.CharField(max_length=10) #Male/Female
    job= models.CharField(max_length=50)
    date_of_birth= models.CharField(max_length=50)
    property_id=models.ForeignKey("Property" , on_delete=models.DO_NOTHING , null=True,blank=True, default=None)
    username=models.ForeignKey( User, on_delete=models.CASCADE,default=None)
    
    def __str__(self):
        return "  NID:"+ self.nid+ '  Name:' + self.first_name +" "+ self.last_name 

class Transaction(models.Model):
    trans_no = models.CharField(max_length=10, primary_key=True,unique=True)
    pid =  models.ForeignKey("Property" , on_delete=models.CASCADE, null=False, default=None)
    client_nid = models.CharField(max_length=50)      
    fname= models.CharField(max_length=50)
    lname= models.CharField(max_length=50)
    account_no= models.CharField(max_length=50)
    amount = models.IntegerField() 
    payment_method=  models.CharField(max_length=50) # Cash / Card / Net Banking
    entry_date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.trans_no
    
class Payment(models.Model):
    booking_date = models.DateTimeField(auto_now_add=True)
    pid =  models.ForeignKey("Property" , on_delete=models.CASCADE, null=False, default=None)
    client_nid =models.CharField(max_length=50)        
    price= models.IntegerField()
    total_paid= models.IntegerField()
    due = models.IntegerField() 
    payment_status=  models.CharField(max_length=50) # Cash / Card / Net Banking
    recent_trans = models.CharField(max_length=10,unique=True)
    
    
    def __str__(self):
        return self.client_nid
    
    

