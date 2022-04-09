from xml.dom.minidom import Document
from xml.etree.ElementInclude import include
from django.conf.urls.static import static
from django.conf import settings
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('cars/', include('cars.urls')),
    path('accounts/', include('accounts.urls')),
    path('socialaccounts/', include('allauth.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)