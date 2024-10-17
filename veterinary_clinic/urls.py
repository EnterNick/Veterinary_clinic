from django.urls import include

from django.urls import path

from . import views
from rest_framework import routers

from .views import UserViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('groups', GroupViewSet)

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('add_request', views.MakeRequestView.as_view()),
    path('', include(router.urls)),
    path('auth', include('rest_framework.urls', namespace='rest_framework'))
]
