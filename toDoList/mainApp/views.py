from django.shortcuts import render
from rest_framework import generics

from .serializers import *
from .models import *

#Read
class ListTodo(generics.ListCreateAPIView):
    queryset = toDoList.objects.all()
    serializer_class = todoSerializer

#Update
class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = toDoList.objects.all()
    serializer_class = todoSerializer

#Create
class CreateTodo(generics.CreateAPIView):
    queryset = toDoList.objects.all()
    serializer_class = todoSerializer

#Delete
class DeleteTodo(generics.DestroyAPIView):
    queryset = toDoList.objects.all()
    serializer_class = todoSerializer

