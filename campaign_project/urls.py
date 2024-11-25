# campaign_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('campaign_app.urls')),  # Including the campaign app URLs
]
