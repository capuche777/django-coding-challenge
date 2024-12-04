from django.http.response import JsonResponse
from django.views import generic
from rest_framework import viewsets
from rest_framework.generics import UpdateAPIView, GenericAPIView
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from checkout.models import Product
from checkout.serializers import ProductSerializer, OrderSerializer
from checkout.utils.custom_decorators import product_exists_required
from checkout.utils.common_functions import calculate_total


class IndexView(generic.TemplateView):
    template_name = "index.html"


class ProductListView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        """
        It returns a list of products.
        """
        queryset = Product.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class ProductUpdateView(UpdateAPIView):
    """
    It will update a product with the given pk, allowed requests methods are PUT and PATCH.
    PUT will update the product and PATCH will partially update it.
    @param: pk
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]


class OrderView(GenericAPIView):
    parser_classes = (JSONParser,)
    authentication_classes = []
    serializer_class = OrderSerializer

    @product_exists_required
    def post(self, request):
        """
        API endpoint that calculates the order total.
        """
        serializer = self.serializer_class(data={'products': request.data})
        serializer.is_valid(raise_exception=True)

        total = calculate_total(serializer.validated_data)
        response_obj = {"total": round(total, 2)}
        return JsonResponse(response_obj, safe=False)
