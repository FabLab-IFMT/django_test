# testeesp32/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('control.urls')),  # Redireciona a raiz para o app 'control'
]
