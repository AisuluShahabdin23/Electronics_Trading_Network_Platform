# Generated by Django 5.0.3 on 2024-03-18 15:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='Производитель')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('country', models.CharField(max_length=150, verbose_name='Страна')),
                ('city', models.CharField(max_length=150, verbose_name='Город')),
                ('street', models.CharField(max_length=150, verbose_name='Улица')),
                ('house_number', models.CharField(max_length=10, verbose_name='Номер дома')),
            ],
            options={
                'verbose_name': 'Производитель',
                'verbose_name_plural': 'Производители',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='Название поставщика')),
                ('email', models.EmailField(blank=True, max_length=150, null=True, unique=True, verbose_name='Электронная почта поставщика')),
                ('supplier_type', models.CharField(choices=[(1, 'Розничная сеть'), (2, 'Индивидуальный предприниматель')], verbose_name='Тип поставщика')),
                ('country', models.CharField(max_length=150, verbose_name='Страна')),
                ('city', models.CharField(max_length=150, verbose_name='Город')),
                ('street', models.CharField(max_length=150, verbose_name='Улица')),
                ('house_number', models.CharField(max_length=10, verbose_name='Номер дома')),
            ],
            options={
                'verbose_name': 'Поставщик',
                'verbose_name_plural': 'Поставщики',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('model', models.CharField(max_length=100, verbose_name='Модель')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата выхода продукта на рынок')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electronic_products_shop.manufacturer', verbose_name='Производитель')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='TradeNetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Наименование торговой сети')),
                ('debt_to_supplier', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Задолженность перед поставщиком')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electronic_products_shop.manufacturer', verbose_name='Производитель')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electronic_products_shop.product', verbose_name='Товар')),
                ('receiver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_receiver', to='electronic_products_shop.supplier', verbose_name='Получатель')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_supplier', to='electronic_products_shop.supplier', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Торговая сеть',
                'verbose_name_plural': 'Торговые сети',
            },
        ),
    ]
