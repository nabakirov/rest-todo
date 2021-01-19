from rest_framework import viewsets
from . import models, serializers as s


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = s.CategorySerializer
    filterset_fields = ('parent_id',)
    search_fields = ('title',)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return models.Category.objects.filter(user=self.request.user).all()
