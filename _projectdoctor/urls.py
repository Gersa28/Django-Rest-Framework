from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')), # Nos da el LogIn, LogOut
    path('', include('app_documentation.urls')),
    # path('', include('app_bookings.urls')),
    # path('', include('app_doctors.urls')),
    # path('', include('app_patients.urls')),
    path("api/", include("api_urls.urls")),    
]