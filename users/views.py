from rest_framework import generics, status
from rest_framework.response import Response

from users.models import User
from users.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """
    Контроллер для создания пользователей
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = True
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)

    def perform_create(self, request, *args, **kwargs):
        data = request.data
        password = data.get('password')
        user = User.object.get(email=data.get('email'))
        user.set_password(password)
        user.save()


class UserUpdateAPIView(generics.UpdateAPIView):
    """
    Контроллер для изменения пользователя
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """
    Контроллер для просмотра пользователя
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()