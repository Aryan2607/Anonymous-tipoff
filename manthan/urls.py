from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from front.views import *
urlpatterns = [
    path('omen/', admin.site.urls),
    path('',FrontPage),
    path('addtipoff',addTipOff),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

