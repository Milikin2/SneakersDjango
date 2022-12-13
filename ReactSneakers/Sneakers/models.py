from django.db import models


# Create your models here.
class Product(models.Model):
    productImg = models.CharField("Путь до картинки", max_length=255)
    productType = models.CharField("Тип товара", max_length=255)
    productTitle = models.CharField("Заголовок", max_length=255)
    productBrand = models.CharField("Бренд", max_length=255)
    productPrice = models.DecimalField("Цена", max_digits=10, decimal_places=2)


class Worker(models.Model):
    workerName = models.CharField("Имя работника", max_length=255)
    workerLastname = models.CharField("Фамилия работника", max_length=255)
    workerPhone = models.CharField("Телефон работника", max_length=255)
    workerEmail = models.CharField("Почта работника", max_length=255)
    workerPos = models.CharField("Должность работника", max_length=255)
    workerSalary = models.DecimalField("Зарплата", max_digits=8, decimal_places=2)


class User(models.Model):
    userName = models.CharField("Имя клиента", max_length=255)
    userLastname = models.CharField("Фамилия клиента", max_length=255)
    userPhone = models.CharField("Телефон клиента", max_length=255)
    userEmail = models.CharField("Почта клиента", max_length=255)
    userLogin = models.CharField("Логин клиента", max_length=255)
    userPassword = models.CharField("Пароль клиента", max_length=255)


class Fav(models.Model):
    productImg = models.CharField("Путь до картинки", max_length=255)
    productType = models.CharField("Тип товара", max_length=255)
    productTitle = models.CharField("Заголовок", max_length=255)
    productBrand = models.CharField("Бренд", max_length=255)
    productPrice = models.DecimalField("Цена", max_digits=6, decimal_places=2)


class Bought(models.Model):
    productImg = models.CharField("Путь до картинки", max_length=255)
    productType = models.CharField("Тип товара", max_length=255)
    productTitle = models.CharField("Заголовок", max_length=255)
    productBrand = models.CharField("Бренд", max_length=255)
    productPrice = models.DecimalField("Цена", max_digits=6, decimal_places=2)
