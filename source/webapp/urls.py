from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('file/<int:pk>/', views.FileDetailView.as_view(), name='file_detail'),
    path('user/<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
]
