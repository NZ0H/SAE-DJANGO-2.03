from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('machines/',views.liste_machines,name='machines'),
    path('personnels/',views.liste_personnels,name='personnels'),
    path('machine/<pk>' ,views.machine_detail_view ,name='machine-detail'),
    path('add-machine/',views.machine_add_form ,name='add-machine'),
    path('del-machine/',views.machine_delete_form ,name='del-machine'),
    path('personnel/<pk>' ,views.personnel_detail_view ,name='personnel-detail'),
    path('add-personnel/',views.personnel_add_form,name='add-personnel'),
    path('del-personnel/',views.personnel_delete_form ,name='del-personnel'),
    path('infastructure/',views.infrastructure ,name='infrastructure'),
    path('feature/',views.check_ip ,name='feature'),
    path('login/', views.login_views, name='login'),
    path('logout/', views.logout_views, name='logout'),
    path('maintenance/',views.maintenance,name='maintenance')
]

