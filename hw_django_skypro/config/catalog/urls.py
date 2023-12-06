from django.urls import path
from .views import HomeView, ContactView, ProductDetailView

app_name = 'catalog'  # Добавляем переменную app_name для пространства имен

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('product/<int:product_id>/',
         ProductDetailView.as_view(), name='product_detail'),
]
