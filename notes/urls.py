from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from .views import (
    NoteList,
    NoteRetrieve,
    NoteCreate,
    NoteUpdate,
    NoteDelete,
)

app_name = 'notes'

urlpatterns = [
    path('', NoteList.as_view(), name='note_list'),
    path('create/', NoteCreate.as_view(), name='note_create'),
    path('edit/<str:slug>/', NoteUpdate.as_view(), name='note_detail_update'),
    path('delete/<str:slug>/', NoteDelete.as_view(), name='note_detail_delete'),
    path('<str:slug>/', NoteRetrieve.as_view(), name='note_retrieve'),
    # path('<int:pk>/', ArticleDetail.as_view(), name='article_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)