from .models import *
from django import forms

class EditProductForm(forms.Form):
    Produkt = forms.ModelChoiceField(queryset=Product.objects.all())
    Ilosc = forms.FloatField()


class NewProductForm(forms.Form):
    Produkt = forms.CharField()


class OrderForm(forms.Form):
    Pizza = forms.ModelChoiceField(queryset=Pizza.objects.all())
    Ilosc = forms.IntegerField()
    Size = forms.ModelChoiceField(queryset=PizzaSize.objects.all())


class NewPizzaForm(forms.Form):
    Pizza = forms.CharField()
    Cena = forms.IntegerField()
