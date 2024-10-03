from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Category, Product
from products.serializers import CategorySerializer, ProductSerializer
from rest_framework.generics import get_object_or_404

@api_view(['GET'])
def category_list(request):
    categories = Category.objects.all().order_by('-popularity')
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def product_list(request):
    """
    List all  products, or create a new product.
    """
    if request.method == 'GET':
        category_id = request.GET.get('category_id')
        if category_id:
            # Get the category object            
            foundCategory = Category.objects.get(id=category_id)        
            # Filter products that belong to the selected category
            products = Product.objects.filter(categories=foundCategory)
        else:
            products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        print("json recieved is:", request.data)
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, id):
    """
    Retrieve, update or delete a code product.
    """
    product = get_object_or_404(Product, id=id)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)