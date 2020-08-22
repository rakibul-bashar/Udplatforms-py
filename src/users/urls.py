from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter

from .views import (AddressViewSet, UserCreateApiView, UserListApiView,
                    UserRUDApiView)

router = DefaultRouter()
router.register(r"address", AddressViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('user/', UserCreateApiView.as_view(), name='create-user'),
    path('users/', UserListApiView.as_view(), name='user-list'),
    re_path(r'^users/(?P<alias>[\w-]+)/$', UserRUDApiView.as_view(), name='user-details'),
]
