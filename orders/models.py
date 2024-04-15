from django.db import models
from indexapp.models import Products, Sections
from django.core.validators import MinLengthValidator

from orders.validators import validate_len_of_tin


class Order(models.Model):
    user_name = models.CharField(max_length=25, blank=True, verbose_name='Ваше имя')
    name_of_organization = models.CharField(max_length=25, verbose_name='')
    tin = models.CharField(max_length=12, validators=[validate_len_of_tin], verbose_name='')

    created = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=12, verbose_name='')
    email = models.EmailField(verbose_name='')
    comment = models.TextField(verbose_name='Комментарий к заказу', blank=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.name_of_organization)



class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    section = models.ForeignKey(Sections, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return '{}'.format(self.id)


