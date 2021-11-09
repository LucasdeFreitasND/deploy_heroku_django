from django.contrib import admin
from django.urls    import path
from django.urls.conf import include
from .views import home, pretinha
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('pretinha',pretinha, name='pretinha')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
