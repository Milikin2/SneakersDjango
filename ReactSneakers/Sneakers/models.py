from django.db import models


# Create your models here.
class Product(models.Model):
    productImg = models.CharField("Путь до картинки", max_length=255)
    productType = models.CharField("Тип товара", max_length=255)
    productTitle = models.CharField("Заголовок", max_length=255)
    productBrand = models.CharField("Бренд", max_length=255)
    productPrice = models.DecimalField("Цена", max_digits=10, decimal_places=2)


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
