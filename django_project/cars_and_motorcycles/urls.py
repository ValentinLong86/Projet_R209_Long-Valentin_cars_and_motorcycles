from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),

    path('cars/', views.listALLCars),
    path('car_update/<int:id>/', views.car_update),
    path('traitement_car_update/<int:id>/', views.traitement_car_update),
    path('delete_car/<int:id>/', views.delete_car),

    path('motorcycles/', views.listALLMotorcycles),
    path('motorcycle_update/<int:id>/', views.motorcycle_update),
    path('traitement_motorcycle_update/<int:id>/', views.traitement_motorcycle_update),
    path('delete_motorcycle/<int:id>/', views.delete_motorcycle),

    path('add_object/', views.add_object),
    path('traitement_add_object/', views.traitement_add_object),

    path('add_marque/', views.add_marque),
    path('traitement_add_marque/', views.traitement_add_marque),
    path('delete_marque/<int:id>/', views.delete_marque),
    path('update_marque/<int:id>/', views.update_marque),
    path('traitement_update_marque/<int:id>/', views.traitement_update_marque),
]
