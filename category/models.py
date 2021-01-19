from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    class Meta:
        db_table = 'category'
        verbose_name = _('category')
        verbose_name_plural = _('categories')
    title = models.CharField(_('title'), max_length=200, null=False)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, null=False, verbose_name=_('category'))
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='children', blank=True,
                               verbose_name=_('parent'))
    creation_date = models.DateTimeField(_('creation date'), null=False, auto_now_add=True)

    def __str__(self):
        return self.title
