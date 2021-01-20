from rest_todo.exceptions import InvalidType


class ActionSerializerClassMixin(object):
    action_serializer_class = {}

    def get_serializer_class(self):
        if self.action_serializer_class and self.action in self.action_serializer_class:
            return self.action_serializer_class[self.action]
        return super(ActionSerializerClassMixin, self).get_serializer_class()


class FilterObjectByUserMixin(object):
    def filter_queryset(self, queryset):
        queryset = queryset.filter(user=self.request.user)
        return super().filter_queryset(queryset)


class FilterObjectByPK(object):
    filter_pk_field = None

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)
        if self.filter_pk_field is None:
            return queryset
        query_param = self.request.query_params.get(self.filter_pk_field)
        if not query_param:
            return queryset
        if query_param.lower() in {'null', 'none'}:
            return queryset.filter(**{f'{self.filter_pk_field}__isnull': True})
        try:
            query_param = int(query_param)
        except ValueError:
            raise InvalidType({self.filter_pk_field: 'pure integer or "null" required'})

        return queryset.filter(**{self.filter_pk_field: query_param})
