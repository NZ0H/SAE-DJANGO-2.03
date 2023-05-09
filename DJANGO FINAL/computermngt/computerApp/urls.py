from django.urls import path 
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('liste-machines',views.liste_ordi,name='liste-machines')
]