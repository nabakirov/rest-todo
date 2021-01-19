from rest_framework import serializers as s
from . import models


class CategorySerializer(s.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('id', 'title', 'creation_date', 'parent')
        read_only_fields = ('creation_date',)
