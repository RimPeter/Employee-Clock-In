from django.urls import path
from . import views
urlpatterns = [
path('', views.home, name=''),
path('my-login/', views.my_login, name='my-login'),
path('dashboard/', views.dashboard, name='dashboard'),
path('my-logout/', views.my_logout, name='my-logout')
]