from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('cars/', views.listALLCars),
    path('motorcycles/', views.listALLMotorcycles),

    path('add_object/', views.add_object),
    path('traitement_add_object/', views.traitement_add_object),

    path('car_update/<int:id>/', views.car_update),
    path('traitement_car_update/<int:id>/', views.traitement_car_update),

    path('motorcycle_update/<int:id>/', views.motorcycle_update),
    path('traitement_motorcycle_update/<int:id>/', views.traitement_motorcycle_update),

    path('delete_car/<int:id>/', views.delete_car),
    path('delete_motorcycle/<int:id>/', views.delete_motorcycle),

    path('add_marque/', views.add_marque),
    path('traitement_add_marque/', views.traitement_add_marque),
]

