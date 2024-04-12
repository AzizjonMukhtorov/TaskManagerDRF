from rest_framework import serializers
from .models import *

class SerializerCustomUser(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class SerializerTask(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'