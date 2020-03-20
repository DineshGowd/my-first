"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include # new

from django.contrib.auth.views import LogoutView

from accounts.views import login_page,register_page,guest_register_view
from addresses.views import checkout_address_create_view,checkout_address_reuse_view

from .views import home_page_old,home_page_new,home_page,contact_page,about_page


# from products.views import (
#     ProductListView,
#     product_list_view,
#     ProductDetailView,
#     ProductDetailSlugView,
#     product_detail_view,
#     ProductFeaturedListView,
#     ProductFeaturedDetailView
#                             )

urlpatterns = [
	path(r'',home_page),
    path(r'old/', home_page_old),
    path(r'home/', home_page_new,name="home"),
    path(r'contact/', contact_page,name="contact"),
    path(r'login/', login_page,name="login"),
    path(r'checkout/address/create/', checkout_address_create_view,name="checkout_address_create"),
    path(r'checkout/address/reuse/', checkout_address_reuse_view,name="checkout_address_reuse"),
    path(r'register/guest/', guest_register_view,name="guest_register"),
    path(r'logout/', LogoutView.as_view(),name="logout"),
    path(r'register/', register_page,name="register"),
    path(r'about/', about_page,name="blog"),
    path(r'products/', include( ("products.urls","products"),namespace="products")),
    path(r'search/', include( ("search.urls","search"),namespace="search")),
    path(r'cart/', include( ("carts.urls","cart"),namespace="cart")),
    # path(r'featured/', ProductFeaturedListView.as_view()), # gets os errors name wrng means
    # path(r'products-fb/', product_list_view),
    # path(r'products/<int:pk>/', ProductDetailView.as_view()),
    # path(r'products/<slug:slug>/', ProductDetailSlugView.as_view()),
    # path(r'featured/<int:pk>/', ProductFeaturedDetailView.as_view()),
    # path(r'products-fb/<int:pk>/', product_detail_view),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
	urlpatterns =urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns =urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)