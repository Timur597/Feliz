# Generated by Django 3.2.3 on 2021-05-28 15:06

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
        ('sale', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaleProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(default=1)),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Дата')),
                ('final_price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Общая цена')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='Продукт')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sale.sale', verbose_name='Продажи')),
            ],
        ),
    ]
