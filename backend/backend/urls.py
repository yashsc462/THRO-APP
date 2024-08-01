"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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


import os
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf import settings
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.landingpage,name = 'landingpage'),
    path('',views.login,name = 'login'),
    path('dashboard',views.dashboard,name = 'dashboard'),
    path('addVendor',views.addVendor,name = 'addVendor'),
    path('addCustomer',views.addCustomer,name = 'addCustomer'),
    path('addCompany',views.addCompany,name = 'addCompany'),
    path('logout/', views.logout, name='logout'),
    path('vendorList/', views.vendorList, name='vendorList'),
    path('addProduct/', views.add_product, name='addProduct'),
    path('vpo/', views.vpo, name='vpo'),
    path('PO/', views.po, name='PO'),
    path('get_product_price/<int:product_id>/', views.get_product_price, name='get_product_price'),
    path('viewvpo',views.viewvpo,name='viewvpo'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


