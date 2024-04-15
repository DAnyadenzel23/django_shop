from django.urls import path
from .views import cart_add, cart_remove, cart_detail, cart_update


urlpatterns = [
    path('detail/', cart_detail, name='cart_detail'),
    path('add/<int:section_id>/<int:product_id>/', cart_add, name='cart_add'),
    path('remove/<int:product_id>/<str:section>/', cart_remove, name='cart_remove'),
    path('update/<int:product_id>/<str:section>/', cart_update, name='cart_update')
]
