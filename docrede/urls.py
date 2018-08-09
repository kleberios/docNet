from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from core import urls as core_urls

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/',     admin.site.urls),
    path('sisdoc/',    auth_views.login, name='login'),
    path('logout/',    auth_views.logout, name='logout'),
    path('', include(core_urls))
]