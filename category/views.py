from rest_framework import viewsets
from . import models, serializers as s
from rest_todo.mixins import FilterObjectByUserMixin, FilterObjectByPK


class CategoryViewSet(FilterObjectByUserMixin,
                      FilterObjectByPK,
                      viewsets.ModelViewSet):
    serializer_class = s.CategorySerializer
    search_fields = ('title',)
    filter_pk_field = 'parent_id'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return models.Category.objects
