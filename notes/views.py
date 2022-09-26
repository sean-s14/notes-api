# Rest Framework
from rest_framework.generics import (
    RetrieveAPIView,
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status

# Custom
from auth2.permissions import IsUserOrAdmin
from .serializers import NoteSerializer
from .models import Note


class NoteList(ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get_queryset(self):
        return super().get_queryset().order_by('-id')


class NoteRetrieve(RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_field = 'slug'


class NoteCreate(CreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteUpdate(UpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (IsUserOrAdmin,)
    lookup_field = 'slug'


class NoteDelete(DestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (IsUserOrAdmin,)
    lookup_field = 'slug'