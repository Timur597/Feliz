# Generated by Django 3.2.3 on 2021-06-01 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
        ('sale', '0003_remove_sale_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saleproduct',
            name='product',
        ),
        migrations.AddField(
            model_name='saleproduct',
            name='product',
            field=models.ManyToManyField(blank=True, to='product.Product', verbose_name='Продукт'),
        ),
    ]
