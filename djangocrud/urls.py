from django.contrib import admin
from django.urls import path
from tareas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('tarea/', views.tarea, name='tarea'),
    path('tareas_completadas/', views.tareas_completadas, name='tareas_completadas'),
    path('crear_tarea/', views.create_tarea, name='crear_tarea'),
    path('detalle_tarea/<int:tarea_id>/', views.tarea_detalle, name='detalle_tarea'),
    path('detalle_tarea/<int:tarea_id>/completada/', views.tarea_completada, name='tarea_completada'),
    path('detalle_tarea/<int:tarea_id>/eliminar/', views.tarea_eliminar, name='eliminar_tarea'),
    path('logout/',views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
]
