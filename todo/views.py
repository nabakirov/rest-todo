from rest_framework import viewsets
from . import models, serializers as s
from rest_todo.mixins import ActionSerializerClassMixin, FilterObjectByUserMixin


class TodoViewSet(ActionSerializerClassMixin,
                  FilterObjectByUserMixin,
                  viewsets.ModelViewSet):
    action_serializer_class = {
        'list': s.ShortTodoSerializer,
        'retrieve': s.TodoSerializer,
    }
    serializer_class = s.TodoRequestSerializer
    filterset_fields = ('category_id', 'schedule', 'is_done')
    search_fields = ('title', 'description')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        if self.action == 'retrieve':
            return models.Todo.objects.select_related('category')
        return models.Todo.objects
