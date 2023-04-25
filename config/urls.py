from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
