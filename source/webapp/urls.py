from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('file/<int:pk>/', views.FileDetailView.as_view(), name='file_detail'),
    path('user/<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
    path('file/', views.FileCreateView.as_view(), name='file_create'),
    path('file/<int:pk>/update/', views.FileUpdateView.as_view(), name='file_update'),
    path('file/<int:pk>/delete/', views.FileDeleteView.as_view(), name='file_delete'),
    path('search_user/', views.SearchUserView.as_view(), name='search_user'),
]
