from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


app_name = 'engineapp'

urlpatterns = [
    path('api/get/<int:pk>/', views.RetrivedDataView.as_view(), name="api_fetch_detail"),
    path('api/request/', views.RetrivedDataView.as_view(), name="api_request_detail"),
]