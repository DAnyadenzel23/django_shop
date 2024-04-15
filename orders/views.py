from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse

from selektro.settings import EMAIL_HOST_USER
from .forms import OrderCreateForm
from cart.views import Cart
from .models import OrderItem
from indexapp.models import Sections




def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)

        if form.is_valid():
            order = form.save()
            message = '  Здравствуйте, Уважаемый(ая) {}, ожидайте обратной связи по Вашему заказу для компании {}:\n'.format(
                form.cleaned_data['user_name'], form.cleaned_data['name_of_organization'])
            for item in cart:
                product = item['product']
                sections = item['sections']
                for section, quantity in sections.items():
                    section_m = Sections.objects.get(section=section)
                    OrderItem.objects.create(order=order,
                                             product=product,
                                             section=section_m,
                                             quantity=quantity)

                    message = f'{message}{product.name} {section_m.section}: {quantity}кг\n'
            message +='\n C уважением к Вам и Вашему делу и наджедой на дальнейшее сотрудничество.'
            subject = 'Заказ на сайте компании Спектр-Электро успешно оформлен!'
            cart.clear()
            send_mail(subject=subject,
                      message=message,
                      from_email=None,
                      recipient_list=[form.cleaned_data['email'], EMAIL_HOST_USER]
            )
            messages.success(request, 'Ваш заказ успешно создан! Ожидайте обратной связи от менеджера.')
            return render(request, 'indexapp/index.html')
        messages.warning(request, 'Неправильно заполнена форма, попробуйте снова!')
        return render(request, 'cart/cart_detail.html', {'form': form})
