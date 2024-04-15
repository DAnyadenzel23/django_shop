from django.core.paginator import Paginator
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.shortcuts import HttpResponse, render, get_object_or_404
from indexapp.models import Products, Categories, Contacts
from cart.forms import CartAddSectionForm



class IndexView(TemplateView):
    template_name = "indexapp/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        return context


class ContactView(ListView):
    model = Contacts
    template_name = 'indexapp/contact.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ContactView, self).get_context_data()
        context['title'] = 'Контакты Спектр-Электро'
        context['contact_data'] = Contacts.objects.all()
        return context


class ProductsView(ListView):
    model = Products
    template_name = "indexapp/products.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsView, self).get_context_data()
        context['title'] = 'Каталог Спектр-Электро'
        context['categories'] = Categories.objects.all()
        return context

    def get_queryset(self):
        queryset = super(ProductsView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset


def product_view_detail(request, slug, page_number=1):
    product = get_object_or_404(Products, slug=slug)
    per_page = 15
    paginator = Paginator(product.sections.all(), per_page)
    sections_paginator = paginator.page(page_number)
    section_add_form = CartAddSectionForm()
    context = {
        'product': product,
        'sections': sections_paginator,
        'section_add_form': section_add_form,
        'title': 'Карточка продукта'
    }

    return render(request, 'indexapp/product_detail.html', context)

