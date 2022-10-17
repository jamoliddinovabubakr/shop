from django import forms


class AddProductForm(forms.Form):
    name = forms.CharField(max_length=255)
    description = forms.CharField(max_length=255)
    price = forms.IntegerField()
    inStock = forms.IntegerField()


class BuyProductForm(forms.Form):
    inStock = forms.IntegerField()


class EditProductForm(forms.Form):
    name = forms.CharField(max_length=255)
    description = forms.CharField(max_length=255)
    price = forms.IntegerField()
    inStock = forms.IntegerField()
