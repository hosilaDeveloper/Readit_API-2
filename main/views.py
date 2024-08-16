from rest_framework import generics, permissions
from .serializers import AuthorSerializer, CategorySerializer, CommentSerializer, HappyClientsSerializer, \
    PostSerializer, TagSerializer, AboutSerializer
from .models import About, Author, Tag, Category, HappyClients, Post, Comment

# Create your views here.


class HomeView(generics.ListAPIView):
    queryset = Post.objects.all().order_by('-id')[:2]
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class TagView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]


class AuthorView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]


class CommentView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        tag = self.request.query_params.get('tag')
        category = self.request.query_params.get('cat')
        q = self.request.query_params.get('q')

        if tag:
            return Post.objects.filter(tags__name=tag)
        if category:
            return Post.objects.filter(category__name=category)
        if q:
            return Post.objects.filter(title__icontaince=q)


class AboutView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    permission_classes = [permissions.IsAuthenticated]

    def about(self):
        extra_info = self.request.query_params.get('extra')

        if extra_info:
            return About.objects.filter(extra__name=extra_info)


class HappyClientsView(generics.ListCreateAPIView):
    queryset = HappyClients.objects.all()
    serializer_class = HappyClientsSerializer
    permission_classes = [permissions.IsAuthenticated]
