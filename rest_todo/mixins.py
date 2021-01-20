
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
