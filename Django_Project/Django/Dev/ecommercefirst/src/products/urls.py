
from django.conf.urls.static import static

from django.urls import path, include # new
 

from .views import (
    ProductListView,
    ProductDetailSlugView,
                    )
urlpatterns = [
    path(r'', ProductListView.as_view(),name="list"),
    path(r'<slug:slug>/', ProductDetailSlugView.as_view(),name="detail"),
  ]
