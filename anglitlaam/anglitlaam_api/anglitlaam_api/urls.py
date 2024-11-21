from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/account/', include('account.urls.portal_account_urls')),  
    path('api/account/otp/', include('account.urls.portal_account_otp_urls')),  
    path('api/account/forget/', include('account.urls.portal_account_forget_urls')),  
    path('api/account/types/', include('account.urls.portal_account_type_urls')),  
    path('api/class-types/', include('account.urls.portal_class_type_urls')), 
]
