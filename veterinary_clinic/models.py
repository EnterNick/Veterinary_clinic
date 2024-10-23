from django.db import models
from django.contrib.auth.models import AbstractUser


class Person(AbstractUser):
    role = models.CharField(default='Клиент', choices=[('client', 'Клитент'), ('moderator', 'Модератор'),
                                                       ('vet', 'Ветеринар')], max_length=9)


class Services(models.Model):
    name = models.CharField('Название', max_length=100)
    description = models.CharField(max_length=500, null=True)
    vet = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f'Услуга: {self.name}, Доктор: {self.vet}'


class Request(models.Model):
    name = models.CharField(max_length=100)
    pet_name = models.CharField(max_length=100)
    service = models.ForeignKey(Services, on_delete=models.CASCADE, null=True)
    email = models.EmailField()
    time = models.TimeField()
    date = models.DateField()

    def __str__(self):
        return f'Заявка ({self.service}'


class Settings(models.Model):
    site_title = models.CharField(max_length=200)
    slogan = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
