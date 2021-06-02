from django.db import models
from branch.models import Branch
from user.models import User
from client.models import Client
from product.models import Product
from datetime import date


class Sale(models.Model):
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    branch = models.ForeignKey(Branch, verbose_name='Филиал', on_delete=models.CASCADE)
    # user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    client = models.ForeignKey(Client, verbose_name='Клиент', on_delete=models.CASCADE)


class SaleProduct(models.Model):
    sale = models.ForeignKey(Sale, verbose_name='Продажи', on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, verbose_name='Продукт', blank=True)
    amount = models.PositiveIntegerField(default=1)
    date = models.DateField(verbose_name='Дата', default=date.today)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена')

    def __str__(self):
        return "Продукт: {} (для продаж)".format(self.product.title)

    def save(self, *args, **kwargs):
        self.final_price = self.amount * self.product.price
        super().save(*args, **kwargs)
