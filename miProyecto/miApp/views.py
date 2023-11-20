from django.shortcuts import render, get_object_or_404, redirect
from .models import Pedido, Producto, Cliente
from .forms import ProductoForm, FormCliente, PedidoForm
import secrets

def index(request):
    return render(request, 'miApp/index.html')

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'miApp/lista_productos.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('miApp:lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'miApp/crear_producto.html', {'form': form})

def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('miApp:lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'miApp/editar_producto.html', {'form': form})

def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        producto.delete()
        return redirect('miApp:lista_productos')
    return render(request, 'miApp/eliminar_producto.html', {'producto': producto})

def mostrar_producto(request, pk):
    producto = Producto.objects.get(pk=pk)
    return render(request, 'miApp/mostrar_producto.html', {'producto': producto})


def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'miApp/clientes.html', {'clientes': clientes})

def agregar_clientes(request):
    form = FormCliente()
    if request.method == 'POST':
        form = FormCliente(request.POST)
        if form.is_valid():
            form.save()
            return redirect('miApp:listado_clientes')

    return render(request, 'miApp/agregar_cliente.html', {'form': form})

def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.delete()
    return redirect('miApp:listado_clientes')

def actualizar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    
    if request.method == 'POST':
        form = FormCliente(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('miApp:listado_clientes')
    else:
        form = FormCliente(instance=cliente)

    return render(request, 'miApp/agregar_cliente.html', {'form': form, 'cliente': cliente})


def lista_pedidos(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            form = PedidoForm()
    else:
        form = PedidoForm()

    pedidos = Pedido.objects.all()
    context = {'form': form, 'pedidos': pedidos}
    return render(request, 'miApp/lista_pedidos.html', context)

def generar_numero_seguimiento():
    return f'NS-{secrets.randbelow(9000) + 1000}'

def crear_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.total = pedido.calcular_total()
            pedido.save()
            return redirect('miApp:lista_pedidos')
    else:
        form = PedidoForm()

    return render(request, 'miApp/crear_pedido.html', {'form': form})

def editar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    
    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('miApp:lista_pedidos')
    else:
        form = PedidoForm(instance=pedido)
    
    return render(request, 'miApp/lista_pedidos.html', {'form': form, 'pedidos': Pedido.objects.all()})

def eliminar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    pedido.delete()
    return redirect('miApp:lista_pedidos')