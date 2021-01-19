from rest_framework import serializers as s
from . import models
from rest_todo.exceptions import ForeignKeyNotFoundError


class CategorySerializer(s.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('id', 'title', 'creation_date', 'parent')
        read_only_fields = ('creation_date',)

    def validate_parent(self, value):
        if value.user_id != self.context['request'].user.id:
            raise ForeignKeyNotFoundError()
        return value
