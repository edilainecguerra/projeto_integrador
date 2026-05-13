from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('L', _('Low')),
        ('M', _('Medium')),
        ('H', _('High')),
    ]

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('User'))
    title = models.CharField(max_length=100, verbose_name=_('Title'))
    description = models.TextField(blank=True, verbose_name=_('Description'))
    due_date = models.DateField(verbose_name=_('Due Date'))
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, verbose_name=_('Priority'))
    completed = models.BooleanField(default=False, verbose_name=_('Completed'))

    class Meta:
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')

    def __str__(self):
        return self.title