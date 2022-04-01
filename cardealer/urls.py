from xml.dom.minidom import Document
from xml.etree.ElementInclude import include
from django.conf.urls.static import static
from django.conf import settings
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('cars/', include('cars.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)