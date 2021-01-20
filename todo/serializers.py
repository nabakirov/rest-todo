from rest_framework import serializers as s
from . import models
from rest_todo.exceptions import ForeignKeyDoesNotExistError
from category.serializers import CategorySerializer


class TodoRequestSerializer(s.ModelSerializer):
    class Meta:
        model = models.Todo
        fields = ('id', 'title', 'category', 'description', 'creation_date', 'schedule', 'is_done')
        read_only_fields = ('creation_date',)

    def validate_category(self, value):
        if value.user.id != self.context['request'].user.id:
            raise ForeignKeyDoesNotExistError()
        return value


class TodoSerializer(s.ModelSerializer):
    class Meta:
        model = models.Todo
        fields = ('id', 'title', 'category', 'description', 'creation_date', 'schedule', 'is_done')
        read_only_fields = ('creation_date',)
    category = CategorySerializer()


class ShortTodoSerializer(s.ModelSerializer):
    class Meta:
        model = models.Todo
        fields = ('id', 'title', 'category', 'creation_date', 'schedule', 'is_done')
        read_only_fields = fields
