from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer, UserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model


class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,) #permisos creado desde permissions.py con regla de negocio para editar
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'author']

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    #(permissions.IsAdminUser,) to inclide permision in this view as general 


class UserList(generics.ListCreateAPIView):  # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):  # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer