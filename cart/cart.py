from decimal import Decimal
from django.conf import settings
from indexapp.models import Products, Sections

class Cart(object):

    def __init__(self, request):
        """
        Инициализация корзины
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {} #Создаем пустую корзину в случае ее отсутствия
        self.cart = cart

    def add(self, product, section, quantity=20, update_quantity=False):
        """
        Добавить продукт в корзину.
        """
        product_id = str(product.id)
        section_name = str(section.section)
        if product_id not in self.cart:
            self.cart[product_id] = {}
            self.cart[product_id]['sections'] = {}
        if section_name not in self.cart[product_id]['sections']:
            self.cart[product_id]['sections'][section_name] = 0


        if update_quantity:
            self.cart[product_id]['sections'][section_name] = quantity
        else:
            self.cart[product_id]['sections'][section_name] += quantity
        self.save()

    def update(self, product, section, quantity):
        '''
        Обновить количество сечения в корзине
        '''
        product_id = str(product.id)
        section_name = str(section.section)
        self.cart[product_id]['sections'][section_name] = quantity
        self.save()


    def save(self):
        # Обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def remove(self, product, section):
        """
        Удаление товара из корзины.
        """
        product_id = str(product.id)
        section_name = str(section.section)
        if product_id in self.cart and section_name in self.cart[product_id]['sections']:
            del self.cart[product_id]['sections'][section_name]
            self.save()

    def __iter__(self):
        """
        Перебор элементов в корзине и получение продуктов из базы данных.
        """
        product_ids = self.cart.keys()

        # получение объектов product и добавление их в корзину
        products = Products.objects.filter(id__in=product_ids)

        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():

            item['product_len'] = len(item['sections']) + 1
            yield item

    def __len__(self):
        """
        Подсчет всего количества товаров в корзине в кг.
        """
        total_quantity = 0
        for product in self.cart.values():
            for section, prod_quant in product['sections'].items():
                total_quantity += prod_quant

        return total_quantity





    def clear(self):
        # удаление корзины из сессии
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

