from django.db import models
from django.utils.translation import gettext_lazy as _


class Todo(models.Model):
    class Meta:
        db_table = 'todo'
        verbose_name = _('todo')
        verbose_name_plural = _('todo')

    title = models.CharField(_('title'), max_length=200, null=False)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, null=False, verbose_name=_('user'),
                             related_name='todo')
    category = models.ForeignKey('category.Category', on_delete=models.CASCADE, related_name='todo',
                                 verbose_name=_('category'), null=True, blank=True)
    description = models.TextField(_('description'), null=True, blank=True)
    creation_date = models.DateTimeField(_('creation date'), null=False, auto_now_add=True)
    schedule = models.DateField(_('schedule'), null=True, blank=True)
    is_done = models.BooleanField(_('is done'), null=False, default=False)

    def __str__(self):
        return self.title
