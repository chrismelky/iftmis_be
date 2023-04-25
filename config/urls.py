from django.contrib import admin
from django.urls import path, re_path, include

from app_auth.custom_auth_response import CustomAuthResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^o/token/$', CustomAuthResponse.as_view(), name='token'),
    re_path(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
