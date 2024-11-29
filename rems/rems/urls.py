
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls')), # Main application URLs
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 


#admin config
admin.site.site_header = " OneGroup6 Administration"  # Customize the site header text in the admin page
admin.site.site_title = "OneGroup6 Admin Portal"   # Customize the top title of the admin portal
admin.site.index_title = "Welcome to OneGroup6 admin portal!"     # Customize the welcome message on the index page