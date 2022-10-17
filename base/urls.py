from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('view-resume/', views.view_resume, name="resume"),
    path('view-crm/', views.view_crm, name="crm"),
    path('view-discord/', views.view_discord, name="discord"),
    path('view-realestate/', views.view_real_estate, name="realestate"),
]