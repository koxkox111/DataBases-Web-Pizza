from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=256, unique=True, null=False)
    volume = models.FloatField(null=False)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=256, unique=True, null=False)
    price = models.PositiveIntegerField(null=False)

    def __str__(self):
        return self.name


class Order(models.Model):
    date = models.DateTimeField(null=False, auto_now=True)

    def __str__(self):
        return str(self.date)
    

class Ingredient(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    pizza = models.ForeignKey(Pizza, null=True, on_delete=models.SET_NULL)
    amount = models.FloatField(null=False)

    def __str__(self):
        return self.product.name + ' - ' +  str(self.amount) +' g '


class PizzaSize(models.Model):
    name = models.CharField(max_length=256, null=False, unique=True)
    priceMultiplier = models.PositiveIntegerField(null=False)
    ingredientMultiplier = models.FloatField(null=False)

    def __str__(self):
        return self.name


class PizzaOrder(models.Model):
    pizza = models.ForeignKey(Pizza, null=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
    size = models.ForeignKey(PizzaSize, null=True, on_delete=models.SET_NULL)
    amount = models.PositiveIntegerField(null=False)

    def __str__(self):
        amo = ''
        if self.amount > 1:
            amo = ' x' + str(self.amount)

        return self.pizza.name + ' ' + self.size.name + amo
