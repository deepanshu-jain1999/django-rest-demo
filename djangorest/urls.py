from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from djangorest import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('apps.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)