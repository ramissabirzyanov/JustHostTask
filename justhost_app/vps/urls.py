from django.urls import path
from . import views

urlpatterns = [
    path('vps/', views.VPSListView.as_view(), name='vps_list'),
    path('vps/create', views.VPSCreateView.as_view(), name='vps_create'),
    path('vps/<uuid:uid>/', views.VPSDetailView.as_view(), name='vps_detail'),
]
