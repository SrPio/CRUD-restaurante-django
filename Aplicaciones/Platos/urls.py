from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registarPlato/', views.registarPlato),
    path('registarAlimento/', views.registarAlimento),
    path('edicionPlato/<codigo>', views.edicionPlato),
    path('editarPlato/', views.editarPlato),
    path('eliminacionPlato/<codigo>', views.eliminacionPlato),
    path('edicionAlimento/<nombre>', views.edicionAlimento),
    path('editarAlimento/', views.editarAlimento),
    path('eliminacionAlimento/<nombre>', views.eliminacionAlimento)
]