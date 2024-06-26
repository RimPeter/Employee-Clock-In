from django.urls import path
from . import views
urlpatterns = [
path('', views.home, name=''),
path('my-login/', views.my_login, name='my-login'),
]