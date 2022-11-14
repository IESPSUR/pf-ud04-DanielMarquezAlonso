from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('tienda/', views.welcome, name='welcome'),
    path('tienda/admin/listado/', views.admin_listado, name='admin_listado'),
    path('tienda/admin/producto_detalle/<int:pk>/', views.admin_producto_detalle, name='admin_producto_detalle'),
    path('tienda/admin/producto_nuevo/', views.admin_producto_nuevo, name='admin_producto_nuevo'),
    path('tienda/admin/producto_eliminar/<int:pk>/', views.admin_producto_eliminar, name='admin_producto_eliminar'),

]
