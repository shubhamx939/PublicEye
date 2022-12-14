from django.urls import path, include
from Account.views import UserDetailAPIView

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
]