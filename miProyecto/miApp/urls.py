from django.urls import path
from . import views
from .views import lista_pedidos

app_name = 'miApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes/', views.lista_clientes, name='listado_clientes'),
    path('agregar_cliente/', views.agregar_clientes, name='agregar_clientes'),
    path('lista_productos/', views.lista_productos, name='lista_productos'),
    path('crear_producto/', views.crear_producto, name='crear_producto'),
    path('editar_producto/<int:pk>/', views.editar_producto, name='editar_producto'),
    path('eliminar_producto/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
    path('mostrar_producto/<int:pk>/', views.mostrar_producto, name='mostrar_producto'),
    path('eliminar_cliente/<int:id>/', views.eliminar_cliente, name='eliminar_cliente'),
    path('actualizar_cliente/<int:id>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('lista_pedidos/', lista_pedidos, name='lista_pedidos'),
    path('editar_pedido/<int:pedido_id>/', views.editar_pedido, name='editar_pedido'),
    path('eliminar_pedido/<int:pedido_id>/', views.eliminar_pedido, name='eliminar_pedido'),
]
