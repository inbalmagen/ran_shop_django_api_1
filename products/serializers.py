from rest_framework import serializers
from products.models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CategorySerializerProduct(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializerProduct(many=True)
    # categories = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'image', 'categories']

    def create(self, validated_data):
        categories = validated_data.pop('categories')
        product = Product.objects.create(**validated_data)
        product.categories.set(categories)
        return product