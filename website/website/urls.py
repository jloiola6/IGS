from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('back.apps.core.urls')),
    path('api/', include('back.apps.api.urls')),
]
