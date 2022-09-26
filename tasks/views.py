# Rest Framework
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

# Custom
from auth2.permissions import IsUserOrAdmin
from .serializers import TaskSerializer
from .models import Task


class TaskList(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        return super().get_queryset().order_by('-id')


class TaskCreate(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskUpdate(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsUserOrAdmin,)
    # lookup_field = 'slug'


class TaskDelete(DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsUserOrAdmin,)
    # lookup_field = 'slug'