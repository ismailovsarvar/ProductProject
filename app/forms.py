from django import forms

from app.models import Customer
from app.models import Product


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.FloatField()
    rating = forms.FloatField()
    discount = forms.IntegerField()
    quantity = forms.IntegerField()


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        # fields = ['name', 'description', 'price', 'rating', 'discount', 'quantity']
        exclude = ()


# CUSTOMER FORM
class CustomerAddForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ()


# class CustomerUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Customer
#         # fields = ['name', 'email', 'phone', 'address', 'joined']
#         exclude = ()
#
#
# class CustomerDeleteForm(forms.ModelForm):
#     customer_id = forms.IntegerField(widget=forms.HiddenInput())
