from django.urls import path
from .views import *


urlpatterns = [
    path('', Home.as_view()),
    path('createtask/', TaskCreateAPI.as_view()),
    path('tasklist/', TaskListAPI.as_view()),
    path('taskdelete/<int:pk>/', TaskDeleteAPI.as_view()),
    path('taskupdate/<int:pk>/', TaskUpdateAPI.as_view()),
    path('usercreate', UserCreateAPI.as_view()),
    path('userlist/', UserListAPI.as_view()),
    path('userdelete/<int:pk>/', UserDeleteAPI.as_view()),
    path('userupdate/<int:pk>/', UserUpdateAPI.as_view()),
]
