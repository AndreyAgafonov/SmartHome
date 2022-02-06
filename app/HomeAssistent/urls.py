"""HomeAssistent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

# from smarthome.views import index, settings_ha

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('' , index, name='index'),
    path('', include('smarthome.urls', namespace='smarthome')),
    path('sign-in/', include('users.urls', namespace='users')),
    # path('dashboard/', include('smarthome.urls', namespace='dashboard')),
    # path('settings/', include('smarthome.urls', namespace='settings_ha')),

         # settings_ha, name='settings'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)