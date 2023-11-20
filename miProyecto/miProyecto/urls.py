from django.contrib import admin
from django.urls import path, include
from miApp.views import index 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('miApp/', include('miApp.urls')),
]
