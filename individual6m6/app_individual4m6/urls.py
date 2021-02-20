from django.urls import path
from . import views

app_name = 'app_individual4m6'

urlpatterns = [
    path('', views.asignatura, name='asignatura'),
    path('<pk>/eliminar_asignatura', views.eliminar_asignatura, name='eliminar_asignatura'),
    path('agregar_asignatura', views.agregar_asignatura, name='agregar_asignatura'),
]