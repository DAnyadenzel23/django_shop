
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from indexapp.views import IndexView, ContactView, ProductsView, product_view_detail

app_name = ('indexapp', 'cart', 'orders')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls')),
    path('', include('indexapp.urls')),
    path('order/', include('orders.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
