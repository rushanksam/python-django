"""
URL configuration for dashboards project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

admin.site.site_header = "Dashboard"
# admin.site.site_title = "raji title"
# admin.site.index_title = "raji index title"
# Admin Site Config
admin.sites.AdminSite.site_header = 'My site admin header'
admin.sites.AdminSite.site_title = 'My site admin title'
admin.sites.AdminSite.index_title = 'Welcome to DashBoard'