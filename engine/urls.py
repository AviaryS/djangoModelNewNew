from django.urls import path
from engine import views

urlpatterns = [
    path('delete/<int:id>/', views.delete, name='delete'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('create/', views.create, name='create'),
    path('', views.home, name='home'),
]