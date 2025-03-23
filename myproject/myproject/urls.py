"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from website import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('page-ao/', views.ao_view, name='ao'),
    path('san-pham/<int:product_id>/', views.chi_tiet_san_pham, name='chi_tiet_san_pham'),
    path('them-vao-gio-hang/<int:product_id>/', views.them_vao_gio_hang, name='them_vao_gio_hang'),
    path('cart/', views.gio_hang, name='gio_hang'),
    path('xoa-san-pham/', views.xoa_san_pham, name='xoa_san_pham'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)