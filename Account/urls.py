from django.urls import path, include
from Account.views import UserDetailAPIView, ToDoOperationsAPIView, ToDoviewerAPIView

urlpatterns = [
    path(
        'create-user/',
        UserDetailAPIView.as_view(),
        name='create-user',
    ),
    path(
        'read-user/',
        UserDetailAPIView.as_view(),
        name='read-user',
    ),
    path(
        'update-user/',
        UserDetailAPIView.as_view(),
        name='update-user',
    ),
    path(
        'delete-user/',
        UserDetailAPIView.as_view(),
        name='delete-user',
    ),
    path(
        'create-todo/',
        ToDoOperationsAPIView.as_view(),
        name='create-todo',
    ),
    path(
        'view-all-todo/',
        ToDoOperationsAPIView.as_view(),
        name='view-all-todo',
    ),
    path(
        'view-user-todo/',
        ToDoviewerAPIView.as_view(),
        name='view-user-todo',
    ),
    path(
        'update-todo/',
        ToDoOperationsAPIView.as_view(),
        name='update-todo',
    ),
]