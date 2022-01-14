from rest_framework import serializers
from .models import *

class todoSerializer(serializers.ModelSerializer):
    class Meta:
        model = toDoList
        fields = ('id', 'Title', 'Describe', 'Date', 'Completed')

