# Generated by Django 4.2.6 on 2023-11-19 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miApp', '0002_alter_pedido_estado_alter_pedido_metodo_pago_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productos', to='miApp.cliente'),
        ),
    ]
