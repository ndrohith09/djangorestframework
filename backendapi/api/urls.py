from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import UserViewSet ,BookViewSet ,WorkerViewSet , EmployeeViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('books', BookViewSet)
router.register('worker', WorkerViewSet)
router.register('employee', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]