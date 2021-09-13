from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='tracker-index'),
    path('contactus/', views.contact_us, name='contactus'),
    path('single/', views.single, name='single'),
]