from rest_framework import generics
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication





class Home(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)    


class TaskCreateAPI(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = SerializerTask
    permission_classes = (IsAuthenticated, )


class TaskListAPI(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = SerializerTask
    permission_classes = (IsAuthenticated, )


class TaskDeleteAPI(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = SerializerTask
    permission_classes = (IsAuthenticated, )


class TaskUpdateAPI(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = SerializerTask
    permission_classes = (IsAuthenticated, )    

class UserCreateAPI(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = SerializerCustomUser
    

class UserListAPI(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = SerializerCustomUser
    permission_classes = (IsAuthenticated, )

class UserDeleteAPI(generics.DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = SerializerCustomUser
    permission_classes = (IsAuthenticated, )    

class UserUpdateAPI(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = SerializerCustomUser
    permission_classes = (IsAuthenticated, )