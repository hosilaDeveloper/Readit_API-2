from rest_framework import serializers
from .models import Comment, Category, HappyClients, Post, Author, About, Tag


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    tag = TagSerializer(many=True)
    comment = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


class HappyClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HappyClients
        fields = '__all__'
