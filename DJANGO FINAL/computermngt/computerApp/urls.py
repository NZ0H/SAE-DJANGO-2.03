from django.urls import path 
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('machines/',views.liste_machines,name='machines'),
    path('personnels/',views.liste_personnels,name='personnels'),
    path('machine/<pk>' ,views.machine_detail_view ,name='machine-detail'),
    path('add-machine/',views.machine_add_form ,name='add-machine'),
]

