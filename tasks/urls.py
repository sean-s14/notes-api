from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from .views import (
    TaskList,
    TaskCreate,
    TaskUpdate,
    TaskDelete,
)

app_name = 'tasks'

urlpatterns = [
    path('', TaskList.as_view(), name='task_list'),
    path('create/', TaskCreate.as_view(), name='task_create'),
    path('edit/<int:pk>/', TaskUpdate.as_view(), name='task_detail_update'),
    path('delete/<int:pk>/', TaskDelete.as_view(), name='task_detail_delete'),
]

urlpatterns = format_suffix_patterns(urlpatterns)