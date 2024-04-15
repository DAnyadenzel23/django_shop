from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('products/', views.ProductsView.as_view(), name='products'),
    path('category/<int:category_id>', views.ProductsView.as_view(), name='category_id'),
    path('products/<slug:slug>/', views.product_view_detail, name='product_detail'),
    path('page/<slug:slug>/<int:page_number>/', views.product_view_detail, name='paginator')

]
