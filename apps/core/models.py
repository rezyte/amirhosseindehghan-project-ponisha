from django.db import models

class TimeSpecificModelBase(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    modified_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True