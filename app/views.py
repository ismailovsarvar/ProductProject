from django.shortcuts import render, redirect, get_object_or_404

from app.forms import ProductModelForm, CustomerAddForm
from app.models import Product, Customer


# from django.urls import reverse_lazy
# from django.views.generic import ListView, UpdateView, DeleteView


# Create your views here.

def index(request):
    products = Product.objects.all().order_by('-id')
    context = {
        'products': products
    }
    return render(request, 'app/index.html', context)


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    attributes = product.get_attributes()
    context = {
        'product': product,
        'attributes': attributes
    }
    return render(request, 'app/product-details.html', context)


# def add_product(request):
#     form = ProductForm()
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         name = request.POST['name']
#         description = request.POST['description']
#         price = request.POST['price']
#         rating = request.POST['rating']
#         discount = request.POST['discount']
#         quantity = request.POST['quantity']
#         product = Product(name=name, description=description, price=price, rating=rating, discount=discount,
#                           quantity=quantity)
#         if form.is_valid():
#             product.save()
#             return redirect('index')
#
#     context = {
#         'form': form
#     }
#     return render(request, 'app/add-product.html', context)

def add_product(request):
    form = ProductModelForm()
    if request.method == 'POST':
        form = ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'app/add-product.html', context)


# CUSTOMER VIEWS
def customer_list(request):
    customers = Customer.objects.all()
    context = {
        'customers': customers,
        'add_customer': add_customer,
        'update_form': CustomerUpdateForm(),
        'delete_form': CustomerDeleteForm()
    }
    return render(request, 'app/customers.html', context)


def add_customer(request):
    form = CustomerAddForm()
    if request.method == 'POST':
        form = CustomerAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_customer')

    context = {
        'form': form,
    }
    return render(request, 'app/customers.html', context)


# def update_customer(request, customer_id):
#     customer = get_object_or_404(Customer, id=customer_id)
#     if request.method == 'POST':
#         form = CustomerUpdateForm(request.POST, instance=customer)
#         if form.is_valid():
#             form.save()
#             return redirect('customer_list')
#     else:
#         form = CustomerUpdateForm(instance=customer)
#         context_1 = {
#             'form': form,
#         }
#     return render(request, 'app/customer_update.html', context_1)
#
#
# def delete_customer(request):
#     if request.method == 'POST':
#         form = CustomerDeleteForm(request.POST)
#         if form.is_valid():
#             customer_id = form.cleaned_data['customer_id']
#             customer = get_object_or_404(Customer, id=customer_id)
#             customer.delete()
#             return redirect('customer_list')
#     return redirect('customer_list')
