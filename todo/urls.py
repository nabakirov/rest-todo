from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path, include


router = DefaultRouter()
router.register('todo', views.TodoViewSet, 'todo')


urlpatterns = [
    path('v1/', include(router.urls)),
]
