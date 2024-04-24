from .models import Todo
from .serializers import TodoSerializer
from rest_framework import generics

# Create your views here.

class ListTodo(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    def get_queryset(self):
        user = self.request.user
        queryset = Todo.objects.filter(user=user)
        return queryset


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    def get_queryset(self):
        user = self.request.user
        queryset = Todo.objects.filter(user=user)
        return queryset
