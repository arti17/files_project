from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('user/<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
]
