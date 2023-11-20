from django.db import models

class Cliente(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=20)
    correo = models.EmailField()
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    numeroCompras = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=50)
    stock = models.PositiveIntegerField()
    tamaño = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    fecha_pedido = models.DateField()
    estado = models.CharField(max_length=40)
    metodo_pago = models.CharField(max_length=40)
    direccion_envio = models.CharField(max_length=100)
    numero_seguimiento = models.CharField(max_length=40)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pedidos')
    productos = models.ManyToManyField(Producto, related_name='pedidos')

    def __str__(self):
        return f"Pedido {self.id} - Cliente: {self.cliente.nombre}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.rut = self.cliente.rut
        super().save(*args, **kwargs)