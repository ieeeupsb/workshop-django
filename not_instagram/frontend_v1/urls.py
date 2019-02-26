from django.urls import path
from frontend_v1 import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='home'),
    path('register/', views.register, name='home'),
]
