from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import Item
from .serializer import ItemSerializer




class ItemList(generics.ListAPIView):
    serializer_class = ItemSerializer


    def get_queryset(self):
        queryset = Item.objects.all()

        # Filtering based on category
        categories_str = self.request.query_params.getlist('category', [])
        categories = []
        if len(categories_str)>0:
            categories = categories_str[0].split(',')

        if categories:
            queryset = queryset.filter(category__in=categories)

        # Filtering based on destination
        destinations_str = self.request.query_params.getlist('destination', [])
        destinations = []
        if len(destinations_str)>0:
            destinations = destinations_str[0].split(',')
        if destinations:
            queryset = queryset.filter(destination__in=destinations)
        print(queryset)

        return queryset
