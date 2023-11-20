from django import forms
from django.core.exceptions import ValidationError
from .models import Producto, Cliente, Pedido

def validate_positive_price(value):
    if value <= 0:
        raise ValidationError('El precio debe ser mayor que cero.')

class ProductoForm(forms.ModelForm):
    precio = forms.DecimalField(validators=[validate_positive_price])

    class Meta:
        model = Producto
        fields = '__all__'

class FormCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class PedidoForm(forms.ModelForm):
    productos = forms.ModelMultipleChoiceField(
        queryset=Producto.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    fecha_pedido = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d']
    )

    
    numero_seguimiento = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=False)

    
    METODOS_PAGO = [
        ('efectivo', 'Efectivo'),
        ('tarjeta_credito', 'Tarjeta de crédito'),
        ('tarjeta_debito', 'Tarjeta de débito'),
        ('transferencia_bancaria', 'Transferencia bancaria'),
        ('paypal', 'PayPal'),
        ('criptomoneda', 'Criptomoneda'),
        ('cheque', 'Cheque'),
        ('pago_movil', 'Pago móvil'),
        ('otro', 'Otro'),
    ]

    metodo_pago = forms.ChoiceField(choices=METODOS_PAGO)

    ESTADOS = [
        ('en_espera', 'En Espera'),
        ('en_revision', 'En Revisión'),
        ('cancelado', 'Cancelado'),
        ('en_ruta', 'En Ruta'),
        ('devuelto', 'Devuelto'),
    ]

    estado = forms.ChoiceField(choices=ESTADOS)


    class Meta:
        model = Pedido
        fields = '__all__'