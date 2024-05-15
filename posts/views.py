from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from django_filters.rest_framework import DjangoFilterBackend


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'author']

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
