from django.contrib import admin
from .models import Cliente, Producto


# Register your models here.
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'categoria')
    list_filter = ('categoria',)  


class ClienteAdmin(admin.ModelAdmin):
    list_display = ['rut','nombre','correo','direccion','telefono','numeroCompras']
    
# Register your models here.
admin.site.register(Cliente)