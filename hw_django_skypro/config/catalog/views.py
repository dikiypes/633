from django.views import View
from django.shortcuts import render
import json


class HomeView(View):
    def get(self, request):
        # Чтение информации о продуктах из JSON-файла
        with open('catalog/data/products.json') as json_file:
            products_data = json.load(json_file)

        context = {
            'products': products_data,
        }

        return render(request, 'catalog/home.html', context)


class ContactView(View):
    def get(self, request):
        return render(request, "catalog/contact.html")


class ProductDetailView(View):
    def get(self, request, product_id):
        with open('catalog/data/products.json') as json_file:
            products_data = json.load(json_file)
            for product_data in products_data:
                if product_data['id'] == product_id:
                    break

        context = {
            'product': product_data,
        }

        return render(request, 'catalog/product_detail.html', context)
