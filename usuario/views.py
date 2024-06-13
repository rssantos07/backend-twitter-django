from django.shortcuts import render, get_object_or_404
from rest_framework.viewsets import ModelViewSet
from usuario.models import Profile, User, Post
from usuario.serializers.usuario_serializer import PostSerializer, UserSerializer, MyTokenObtainPairSerializer, RegisterSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_token_data(self, user):
        if user.is_authenticated:
            token_data = MyTokenObtainPairSerializer.get_token(user)
            return {
                'full_name': token_data.get('full_name', ''),
                'username': token_data.get('username', ''),
                'email': token_data.get('email', ''),
                'bio': token_data.get('bio', ''),
                'image': token_data.get('image', ''),
                'verified': token_data.get('verified', False),
            }
        return {}

    def list(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=request.user.pk)
        serializer = self.get_serializer(user)
        token_data = self.get_token_data(request.user)
        return Response([{'users': serializer.data, 'token_data': token_data}], status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        token_data = self.get_token_data(request.user)
        return Response({'user': serializer.data, 'token_data': token_data}, status=status.HTTP_200_OK)


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token/',
        '/api/register/',
        '/api/token/refresh/'
    ]
    return Response(routes)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def testEndPoint(request):
    if request.method == 'GET':
        data = f'Congratulation {request.user}, your API just responded to GET request'
        return Response({'response': data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = request.POST.get('text')
        data = f'Congratulation your API just responded to POST request with text: {text}'
        return Response({'response': data}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        response_data = {
            'mensagem': 'Post criado com sucesso!',
            'data': serializer.data
        }
        
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)
 