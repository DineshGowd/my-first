
from django.conf.urls.static import static

from django.urls import path, include # new


from .views import SearchProductView   

urlpatterns = [
    path(r'', SearchProductView.as_view(),name="query"),
  ]
