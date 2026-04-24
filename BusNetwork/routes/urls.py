from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:route_id>/', views.route_detail, name='route_detail'),
    path('<int:route_id>/book/', views.book, name='book'),
    path('register/', views.register, name='register'),
    path('bookings/', views.my_bookings, name='my_bookings'),
    path('station/<int:station_id>/', views.station_detail, name='station_detail'),
]