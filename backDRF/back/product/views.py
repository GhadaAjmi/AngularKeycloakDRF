from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from requests import request
from rest_framework.decorators import api_view
from rest_framework.response import Response

from back.authentication import KeyCloakAuthentication
from .serializers import ProductSerializer
from product.models import Product
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


    # Token valide, continuer le traitement

    # Token invalide, gérer l'erreur
#Create your views here.
class ProductListView(APIView):
    authentication_classes = [KeyCloakAuthentication]

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({"products": serializer.data})


























