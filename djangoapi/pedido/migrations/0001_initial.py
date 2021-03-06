# Generated by Django 2.1.7 on 2019-03-08 01:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produto', '0003_auto_20190307_0720'),
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(verbose_name='Quantidade')),
                ('preco_unitario', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço Unitário')),
                ('created_at', models.DateTimeField()),
                ('update_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.Client')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='pedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedido.Pedido'),
        ),
        migrations.AddField(
            model_name='item',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.Produto'),
        ),
    ]
