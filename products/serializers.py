from rest_framework import serializers
from products.models import Cart, Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CategorySerializerProduct(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ProductSerializerGet(serializers.ModelSerializer):
    categories = CategorySerializerProduct(many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'image', 'categories']

class ProductSerializer(serializers.ModelSerializer):
    # categories = CategorySerializer(many=True)
    # categories = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'image', 'categories']

    def create(self, validated_data):
        categories = validated_data.pop('categories')
        product = Product.objects.create(**validated_data)
        product.categories.set(categories)
        return product

class CartSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'products', 'total_price']

    def get_total_price(self, obj):
        return obj.total_price()