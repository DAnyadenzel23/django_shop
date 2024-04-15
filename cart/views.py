from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.shortcuts import HttpResponseRedirect
from django.views.decorators.http import require_POST
from indexapp.models import Sections, Products
from orders.forms import OrderCreateForm
from .cart import Cart
from .forms import CartAddSectionForm, CartUpdateSectionForm



@require_POST
def cart_add(request, section_id, product_id):
    cart = Cart(request)
    section = get_object_or_404(Sections, id=section_id)
    product = get_object_or_404(Products, id=product_id)
    form = CartAddSectionForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(section=section,
                 product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
        messages.info(request, '{} {} - {}кг успешно добавлен в Корзину!'.format(product, section, cd['quantity']))


    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def cart_remove(request, section, product_id):
    cart = Cart(request)
    section = get_object_or_404(Sections, section=section)
    product = get_object_or_404(Products, id=product_id)
    cart.remove(product, section)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def cart_update(request, section, product_id):
    cart = Cart(request)
    section = get_object_or_404(Sections, section=section)
    product = get_object_or_404(Products, id=product_id)
    form = CartUpdateSectionForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.update(section=section,
                    product=product,
                    quantity=cd['quantity'])

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def cart_detail(request):
    cart = Cart(request)
    section_update_form = CartUpdateSectionForm()
    order_form = OrderCreateForm()

    context = {'cart': cart,
               'section_update_form': section_update_form,
               'form': order_form
               }


    return render(request, 'cart/cart_detail.html', context)
