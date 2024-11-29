from django.urls import path 
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    
    path('employee_signinup',views.employee_signinup,name='employee_signinup'),
    path('employee_signup',views.employee_signup,name='employee_signup'),
    
    path('signin',views.signin,name='signin'),
    path('signup',views.signup,name='signup'),
    path('ContactUs',views.ContactUs,name='ContactUs'),
    path('AboutUs',views.AboutUs,name='AboutUs'),
    
    #employee
    path('dash_employee',views.dash_employee,name='dash_employee'),
    path('add_property',views.add_property,name='add_property'),
    path('add_rental',views.add_rental ,name='add_rental'),
    path('view_property',views.view_property ,name='view_property'),
    path('view_property_rent',views.view_property_rent ,name='view_property_rent'),
  
    
    path('client_booking',views.client_booking ,name='client_booking'),
    path('client_info',views.client_info ,name='client_info'),
    path('payment_info',views.payment_info ,name='payment_info'),
    path('view_employee',views.view_employee,name='view_employee'),
    path('transaction',views.transaction ,name='transaction'),
    path('update_property',views.update_property ,name='update_property'),
    path('update_rental',views.update_rental ,name='update_rental'),
    
    #user
    path('dash_user',views.dash_user,name='dash_user'),
    path('product_view_user',views.product_view_user,name='product_view_user'),
    path('onebhk',views.onebhk,name='onebhk'),
    path('twobhk',views.twobhk,name='twobhk'),
    path('threebhk',views.threebhk,name='threebhk'),
    path('fourbhk',views.fourbhk,name='fourbhk'),
    path('fivebhk',views.fivebhk,name='fivebhk'),
    path('prop_detail',views.prop_detail,name='prop_detail'),
    path('prop_detail_buy',views.prop_detail_buy,name='prop_detail_buy'),
    
    path('booking_info',views.booking_info,name='booking_info'),
    path('pay',views.pay,name='pay'),
    path('add_post',views.add_post,name='add_post'),
    path('my_ads_user',views.my_ads_user,name='my_ads_user'),
    path('my_info',views.my_info,name='my_info'),
    
    ]