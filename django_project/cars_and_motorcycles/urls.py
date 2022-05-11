from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),

    path('cars/', views.list_all_cars),
    path('car_update/<int:id>/', views.car_update),
    path('t_car_update/<int:id>/', views.t_car_update),
    path('delete_car/<int:id>/', views.delete_car),

    path('motorcycles/', views.list_all_Motorcycles),
    path('motorcycle_update/<int:id>/', views.motorcycle_update),
    path('t_motorcycle_update/<int:id>/', views.t_motorcycle_update),
    path('delete_motorcycle/<int:id>/', views.delete_motorcycle),

    path('add_object/', views.add_object),
    path('t_add_object/', views.t_add_object),

    path('add_marque/', views.add_marque),
    path('t_add_marque/', views.t_add_marque),
    path('delete_marque/<int:id>/', views.delete_marque),
    path('update_marque/<int:id>/', views.update_marque),
    path('t_update_marque/<int:id>/', views.t_update_marque),
]
