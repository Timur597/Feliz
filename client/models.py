from django.db import models
from user.models import User

class Client(models.Model):
    user = models.OneToOneField(User, verbose_name='Клиент', on_delete=models.CASCADE)