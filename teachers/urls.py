from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='teachers/login.html'), name='login'),
    path('logout/',  views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]