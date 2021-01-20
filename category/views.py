from rest_framework import viewsets
from . import models, serializers as s
from rest_todo.mixins import FilterObjectByUserMixin, FilterObjectByPK
from rest_framework.decorators import action
from rest_framework.response import Response


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

    def _tree_representation(self, parent_id, queryset):
        data = {}
        children = []
        for category in queryset:
            if category.id == parent_id:
                data = self.get_serializer(instance=category).data
            elif category.parent_id == parent_id:
                children.append(self._tree_representation(category.id, queryset))
        data['children'] = children
        return data

    @action(methods=('GET',), detail=False, url_path='tree')
    def tree(self, request):
        queryset = self.get_queryset().filter(user=self.request.user).all()
        data = self._tree_representation(None, queryset)
        return Response(data['children'])
